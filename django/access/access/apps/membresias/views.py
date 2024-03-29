#encoding:utf-8
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse , HttpResponseRedirect
from django.contrib.auth.decorators import login_required
#Modelos 
from django.contrib.auth.models import User
from access.apps.membresias.models import membresia,rel_mem,MenoresEdad,PaseMenor
from access.apps.actividades.models import actividad
# Formularios
from access.apps.membresias.forms import frmComMem,UserEditForm,editUserFrm,frmActualizaMembresia,frmMenoresEdad,frmCompraMembresiaOnline,frmCompraMembresiaCallCenter,frmActivaMembresia,frmInfoActivacion,registerUserFrm,frmPaseMenor
from django.contrib.auth.forms import PasswordChangeForm
from django.forms.formsets import formset_factory

# Librerias / Herramientas
from string import digits, letters
import random
from random import choice
from django.core.mail import EmailMultiAlternatives 
import datetime

''' Herramientas '''
def _pw(length=5):
    s = ''
    for i in range(length):
        s += random.choice(letters)
    return s

# Funciones/Herramientas
def add_act(_miembro,texto=""):
	_texto = str(texto)
	try:
		objAct = actividad(miembro=_miembro,descripcion=_texto)
		objAct.save()
		return True
	except Exception, e:
		return False

@login_required
def edit_mem(request):
	objMem = get_object_or_404(membresia,miembro=request.user)
	if request.method == 'POST':
		frm = frmActualizaMembresia(request.POST ,instance=objMem)
		if frm.is_valid():
			frm.save()
			
			nombre = frm.cleaned_data.get('nombre')
			apaterno = frm.cleaned_data.get('apellido_paterno')
			amaterno = frm.cleaned_data.get('apellido_materno')
			email = frm.cleaned_data.get('email')

			_usr = User.objects.get(pk=request.user.pk)
			_usr.first_name = "%s" % nombre
			_usr.last_name = "%s %s" %(apaterno, amaterno)
			_usr.email = "%s" % email
			_usr.save()
			return HttpResponseRedirect('/citas/')
		else:
			ctx ={'form':frm}
			return render_to_response('forms/membresia/edicion.html',ctx,context_instance=RequestContext(request))
	else:
		ctx ={'form':frmActualizaMembresia(instance=objMem)}
		return render_to_response('forms/membresia/edicion.html',ctx,context_instance=RequestContext(request))

@login_required
def reset_pass(request):
	if request.method == 'POST':
		form = PasswordChangeForm(request.user,data=request.POST)
		if form.is_valid():
			form.save()
			ctx = {'msg':'Su nueva contraseña se ha guardado satisfactoriamente'}
			return render_to_response('forms/membresia/reset_pass.html',ctx,context_instance=RequestContext(request))
		else:
			ctx = {'frm':form}
	else:
		ctx = {'frm':PasswordChangeForm(request.user)}
	return render_to_response('forms/membresia/reset_pass.html',ctx,context_instance=RequestContext(request))


def compra_cantidad(request):
	from access.apps.membresias.forms import frmCantidad
	if request.method == 'POST':
		frm =frmCantidad(request.POST)
		if frm.is_valid():
			cantidad = frm.cleaned_data.get('cantidad',0)
			return HttpResponseRedirect('/membresia.compra/%s/'%cantidad)
		else:
			ctx = {'form':frm}
	else:
		ctx = {'form':frmCantidad}
	return render_to_response('forms/membresia/cantidad.html',ctx,context_instance=RequestContext(request))


def compra_multiple(request,cant=0):
	cantidad = int(cant)
	if cantidad > 9 or cantidad < 1:
		return HttpResponseRedirect('/membresia.corporativa/')
	MemFormSet = formset_factory(frmComMem,extra=cantidad)
	if request.method == 'POST':
		frm = MemFormSet(request.POST)
		if frm.is_valid():
			if request.user.is_authenticated():
				objMem = get_object_or_404(membresia,miembro=request.user)
				idsMemCompradas = []
				for Mem in frm:
					NewMem = Mem.save(commit=False)
					NewMem.tipo = 1
					NewMem.password = _pw()
					NewMem.costo = 1575.00 * 0.85
					NewMem.padre = objMem.id
					NewMem.save()
					idsMemCompradas.append(NewMem.id)
					# Se agrega relacion de titular y referido
					objRel = rel_mem(titular=request.user,mem_titular=objMem,mem_referido=NewMem)
					objRel.save()
				
				request.session['memcompradas'] = idsMemCompradas
				print idsMemCompradas
				request.session['MemPadre'] = objMem.id
				return HttpResponseRedirect('/membresia.resumen/multiple/')
			else:
				cont = 1
				padre = 0
				for Mem in frm:
					NewMem = Mem.save(commit=False)
					NewMem.tipo = 1
					NewMem.password = _pw()
					NewMem.costo = 1575.00
					if cont != 1:
						NewMem.costo = 1575 * 0.85
						NewMem.padre = padre
					NewMem.save()
					if cont == 1:
						padre = NewMem.id
						request.session['MemPadre'] = padre
					cont = cont + 1
				return HttpResponseRedirect('/membresia.resumen/multiple/')
		else:
			objForm = frm	
			ctx = {'frmSet':objForm}
			return render_to_response('forms/membresia/compra_multiple.html',ctx,context_instance=RequestContext(request))
	else:
		objForm = MemFormSet()
		ctx = {'frmSet':objForm}
		return render_to_response('forms/membresia/compra_multiple.html',ctx,context_instance=RequestContext(request))


def ResumenCompraMultiple(request):
	idMem = int(request.session.get('MemPadre', 0))
	try:
		MemTitular = membresia.objects.get(pk=idMem)
		if request.user.is_authenticated():
			listId = request.session.get('memcompradas')
			MemCompradas = membresia.objects.filter(pk__in=listId)
		else:
			MemCompradas = membresia.objects.filter(padre=idMem,fecha_registro=datetime.date.today())
	except:
		return HttpResponseRedirect("/")

	if request.method == "POST":
		cancela = request.POST.get('cancela',"0")
		if cancela == "1":
			MemTitular.delete()
			if MemCompradas:
				for mem in MemCompradas:
					mem.delete()
			return HttpResponseRedirect("/")
		else:
			if not request.user.is_authenticated():
				_envia_email_compra(MemTitular)
			if MemCompradas:
				for mem in MemCompradas:
					_envia_email_compra(mem)
			if request.user.is_authenticated():
				return HttpResponseRedirect("/membresia.referidos/")
			else:
				return HttpResponseRedirect("/")
	else:
		
		total = 0
		for mem in MemCompradas:
			total += mem.costo

		if not request.user.is_authenticated():
			total += 1575
		
		ctx = {'objMem':MemTitular,'objMems':MemCompradas,'tot':total}
		return render_to_response('membresia/resumen_compra_multiple.html',ctx,context_instance=RequestContext(request))


def EnviaEmailMultiple(objMem):
	to_mem_dos = ""
	try:
		to_mem = objMem.email
		subject = "24 Access Membresia"
		html_content = "Bienvenido a 24Access, gracias por su compra.<br><br>Para activar entra aqui <a href='http://desarrollo.newemage.com:8888/membresia.inicio/'>http://desarrollo.newemage.com:8888/membresia.inicio/</a> <br><br> Este es tu numero de membresia %s <br> Este es tu password %s " %(objMem.id , objMem.password)
		msg = EmailMultiAlternatives(subject,html_content,'from@server.com',[to_mem])
		msg.attach_alternative(html_content,'text/html') #Definimos el contenido como HTML
		msg.send() #enviamos el correo	
		return True
	except:
		return False


def compra_membresia_online(request):
	if request.method == "POST":
		frm = frmCompraMembresiaOnline(request.POST)
		if frm.is_valid():
			newMem = frm.save(commit=False)
			newMem.online = True
			objMembresia = newMem.save()
			request.session['pkMem'] = newMem.id
			return HttpResponseRedirect('/membresia.resumen/')
		else:
			objForm = frm			
	else:
		objForm = frmCompraMembresiaOnline()
	
	ctx = {'form':objForm}
	return render_to_response('forms/membresia/compra.html',ctx,context_instance=RequestContext(request))



def sel_tipo_mem(request):
	return render_to_response('forms/membresia/pre_compra.html',context_instance=RequestContext(request))


def mem_tipo(request,id_tipo):
	tipo = int(id_tipo)
	if tipo == 1:
		request.session['tipo_mem'] = 1
	elif tipo == 2:
		request.session['tipo_mem'] = 2
	elif tipo == 3:
		request.session['tipo_mem'] = 3
	else:
		request.session['tipo_mem'] = 4
	return HttpResponseRedirect("/membresia.compra/callcenter/")



def compra_membresia_call_center(request):
	idtipo = int(request.session.get('tipo_mem',4))
	if idtipo == 4:
		return HttpResponseRedirect("/membresia.compra/tipo/")
	
	if request.method == "POST":
		frm = frmCompraMembresiaCallCenter(request.POST)
		if frm.is_valid():
			newMem = frm.save(commit=False)
			newMem.password = _pw()
			objMembresia = newMem.save()

			request.session['pkMem'] = newMem.id
			return HttpResponseRedirect('/membresia.resumen/')
		else:
			objForm = frm			
	else:
		objForm = frmCompraMembresiaCallCenter()
	ctx = {'form':objForm,'tipo':idtipo}
	return render_to_response('forms/membresia/compra.html',ctx,context_instance=RequestContext(request))

@login_required(login_url='/usuarios/login/')
def referidos_vista(request):
	try:
		objRel = rel_mem.objects.filter(titular=request.user)
	except Exception, e:
		objRel = None
	ctx = {'objRel':objRel,'rango':xrange(objRel.count(),9)}
	return render_to_response('referidos/membresias.html',ctx,context_instance=RequestContext(request))	

@login_required(login_url='/usuarios/login/')
def compra_referido(request):
	idtipo = 1
	try:
		objRel = rel_mem.objects.filter(titular=request.user).count()
	except Exception, e:
		objRel = None
	
	if objRel >= 9:
		ctx ={'objMensaje':"No puedes agregar a mas de 9 membresias, para esto habla con uno de nuestros call center, quien te asesorara para migrar a tipo corporativo."}
		return render_to_response('mensaje/mensaje.html',ctx,context_instance=RequestContext(request)) 

	if request.method == "POST":
		frm = frmCompraMembresiaCallCenter(request.POST)
		if frm.is_valid():
			newMem = frm.save(commit=False)
			newMem.password = _pw()
			newMem.save()
			request.session['pkMem'] = newMem.id
			# Agrega relacion de referidos
			objMemTit = get_object_or_404(membresia,miembro=request.user)
			objRel = rel_mem(titular=request.user,mem_titular=objMemTit,mem_referido=newMem)
			objRel.save()
			# Agrega activiadad
			texto = "Usted a comprado una nueva membresia con el id %s" % newMem.id
			add_act(request.user,texto)
			# Muestra resumen
			return HttpResponseRedirect('/membresia.resumen/')
		else:
			objForm = frm			
	else:
		objForm = frmCompraMembresiaCallCenter()
	ctx = {'form':objForm,'tipo':idtipo}
	return render_to_response('forms/membresia/compra_referido.html',ctx,context_instance=RequestContext(request))	



def resumen_compra(request):
	idMem = int(request.session.get('pkMem', 0))
	try:
		objMembresia = membresia.objects.get(pk=idMem)
	except:
		return HttpResponseRedirect("/")

	if request.method == "POST":
		cancela = request.POST.get('cancela',"0")
		if cancela == "1":
			objMembresia.delete()
			return HttpResponseRedirect("/")
		else:
			_envia_email_compra(objMembresia)
			return HttpResponseRedirect("/")
	else:
		ctx = {'objMem':objMembresia}
		return render_to_response('membresia/resumen_compra.html',ctx,context_instance=RequestContext(request))


def _envia_email_compra(objMem):
	to_mem_dos = ""
	try:
		to_mem = objMem.email
		subject = "24 Access Membresia"
		html_content = "Bienvenido a 24Access, gracias por su compra.<br><br>Para activar entra aqui <a href='http://desarrollo.newemage.com:8888/membresia.inicio/'>http://desarrollo.newemage.com:8888/membresia.inicio/</a> <br><br> Este es tu numero de membresia %s <br> Este es tu password %s " %(objMem.id , objMem.password)
		msg = EmailMultiAlternatives(subject,html_content,'from@server.com',[to_mem])
		msg.attach_alternative(html_content,'text/html') #Definimos el contenido como HTML
		msg.send() #enviamos el correo	
		return True
	except:
		return False
	


def activa_membresia_login(request):
	if request.method == "POST":
		frm = frmActivaMembresia(request.POST)
		if frm.is_valid():
			_mem  = int(frm.cleaned_data['membresia'])
			_pass = frm.cleaned_data['password']
			try:
				objMem = membresia.objects.get(pk=_mem,password=_pass)
			except:
				objMem = None
	
			if objMem:
				if objMem.padre != 0:
					try:
						objPadre = membresia.objects.get(pk=objMem.padre)
					except:
						objPadre = None

					if objPadre:
						if not objPadre.activa:
							return render_to_response('mensaje/mensaje.html',{'objMensaje':'La membresia titular debe activar primero.'},context_instance=RequestContext(request))
				else:
					objPadre = None

				request.session['membresia_id'] = objMem.id
				return HttpResponseRedirect('/membresia.activa/')
			else:
				ctx = {'frmActiva':frm,'mensaje':"Por favor verifique sus datos de activación"}
				return render_to_response('forms/membresia/login_activa.html',ctx,context_instance=RequestContext(request))
		else:
			ctx = {'frmActiva':frm}
	else:
		ctx = {'frmActiva':frmActivaMembresia}
	return render_to_response('forms/membresia/login_activa.html',ctx,context_instance=RequestContext(request))


def activa_membresia_update(request):
	idMem = int(request.session.get('membresia_id', 0))
	try:
		objMembresia = membresia.objects.get(pk=idMem)
	except:
		return HttpResponseRedirect("/")

	if request.method == "POST":
		frmReg 	= registerUserFrm(request.POST)
		frm 	= frmInfoActivacion(request.POST)
		if frm.is_valid() and frmReg.is_valid():
			# Crea usuario nuevo para inicio de sesion
			user_name = frmReg.cleaned_data['username']
			password_ = frmReg.cleaned_data['password']
			email_    = objMembresia.email
			new_user  = User.objects.create_user(username=user_name,password= password_,email=email_)
			new_user.first_name = objMembresia.nombre
			new_user.last_name 	= "%s %s" %(objMembresia.apellido_paterno,objMembresia.apellido_materno)
			new_user.is_staff = False
			new_user.save()
			# Actualiza info de Membresia
			objMembresia.miembro = new_user
			objMembresia.activa = True
			objMembresia.renovo_pass = True
			objMembresia.save()
			# Edita y guarda info adicional
			frmAdicional = frm.save(commit=False)
			frmAdicional.membresia = objMembresia
			frmAdicional.save()
			# Agrega relaciones de membresias adicionales
			# rel_mem
			try:
				MemAdicionales = membresia.objects.filter(padre=objMembresia.id)
			except:
				MemAdicionales = None

			if MemAdicionales:
				for MemAdicional in MemAdicionales:
					new_rel = rel_mem(titular=new_user,mem_titular=objMembresia,mem_referido=MemAdicional)
					new_rel.save()


			# Envio de email de confirmacion de registro
			_envia_email_registro(new_user)			
			# Se redirecciona al login para usuarios
			return HttpResponseRedirect("/usuarios/login/")
		ctx = {'frmActiva':frm,'frmR':frmReg}
	else:
		frmReg = registerUserFrm()
		frm = frmInfoActivacion()
		ctx = {'frmActiva':frmInfoActivacion,'frmR':frmReg}
	return render_to_response('forms/membresia/activa_membresia.html',ctx,context_instance=RequestContext(request))


def _envia_email_registro(objUser):
	to_mem_dos = ""
	try:
		to_mem = objUser.email
		subject = "24 Access Membresia"
		html_content = "Bienvenido de nuevo a 24Access, gracias por activar su membresía.<br><br>Para entrar al sistema y solicitar tus citas entra aquí <a href='http://desarrollo.newemage.com:8888/usuarios/login/'>http://desarrollo.newemage.com:8888/usuarios/login/</a> <br><br> Este es su usuario %s" % objUser.username
		msg = EmailMultiAlternatives(subject,html_content,'from@server.com',[to_mem])
		msg.attach_alternative(html_content,'text/html') #Definimos el contenido como HTML
		msg.send() #enviamos el correo	
		return True
	except:
		return False

def _envia_email_menores(objUser,menor):
	to_mem_dos = ""
	try:
		to_mem = objUser.email
		subject = "24 Access Membresia"
		html_content = "Se ha agregado nu nuevo menor de edad con el nombre de %s %s %s" % (menor.nombre,menor.apellido_paterno,menor.apellido_materno)
		msg = EmailMultiAlternatives(subject,html_content,'from@server.com',[to_mem])
		msg.attach_alternative(html_content,'text/html') #Definimos el contenido como HTML
		msg.send() #enviamos el correo	
		return True
	except:
		return False


@login_required
def menores_edad_all(request):
	from datetime import date,timedelta
	qs = MenoresEdad.objects.prefetch_related('Pases').filter(titular=request.user)

	ctx = {'objMenores':qs,'fecha_hoy':date.today()}
	return render_to_response('menores/menores.html',ctx,context_instance=RequestContext(request))

@login_required
def menores_edad_nuevo(request):
	if request.method == "POST":
		frm = frmMenoresEdad(request.POST)
		if frm.is_valid():
			_frm = frm.save(commit=False)
			_frm.titular = request.user
			
			mem = membresia.objects.get(miembro=request.user)
			try:
				mem = membresia.objects.get(miembro=request.user)
			except Exception, e:
				mem = None

			print mem
			_frm.mem_titular = mem
			_frm.save()
			_envia_email_menores(request.user,_frm)

			# Agrega activiadad
			texto = "Se agrego un nuevo menor de edad a su lista"
			add_act(request.user,texto)
			return HttpResponseRedirect("/membresia.menor/")
		else:
			ctx = {'form':frm}
	else:
		frm = frmMenoresEdad()
		ctx = {'form':frm}
	return render_to_response('menores/nuevo.html',ctx,context_instance=RequestContext(request))

@login_required
def compra_pase(request):
	import datetime
	from django.utils import timezone
	
	_menores = MenoresEdad.objects.filter(titular=request.user)
	if request.method == "POST":
		frm = frmPaseMenor(request.POST)
		if frm.is_valid():
			_menor = frm.cleaned_data['menor']
			try:
				objPases = PaseMenor.objects.filter(titular=request.user, menor=_menor)
				print objPases
				if objPases:
					for p in objPases:
						if p.fecha_fin > datetime.datetime.now().date():
							ctx = {'form':frm,'mensaje':"Este menor de edad tiene un pase valido",'pase':p}
							return render_to_response('menores/pase.html',ctx,context_instance=RequestContext(request))
			except Exception, e:
				print "Error"
				pass

			_frm = frm.save(commit=False)
			
			#  Obtengo fecha actual y se le suma un año
			_fin = timezone.now() + datetime.timedelta(days=365)
			
			# Asignacion de valores a las variables
			_frm.titular = request.user
			_frm.fecha_fin = _fin
			_frm.save()
			
			_envia_email_menores_pase(request.user,_frm)

			# Agrega activiadad
			texto = "Se compro un pase de menor de edad para un año"
			add_act(request.user,texto)
			return HttpResponseRedirect("/membresia.menor/")
		else:
			ctx = {'form':frm,'menores':_menores}
	else:
		frm = frmPaseMenor()
		ctx = {'form':frm,'menores':_menores}
	return render_to_response('menores/pase.html',ctx,context_instance=RequestContext(request))


def _envia_email_menores_pase(objUser,menor):
	to_mem_dos = ""
	try:
		to_mem = objUser.email
		subject = "24 Access Membresia"
		html_content = "Se a comprado un pase por un año para  %s %s %s" % (menor.nombre,menor.apellido_paterno,menor.apellido_materno)
		msg = EmailMultiAlternatives(subject,html_content,'from@server.com',[to_mem])
		msg.attach_alternative(html_content,'text/html') #Definimos el contenido como HTML
		msg.send() #enviamos el correo	
		return True
	except:
		return False