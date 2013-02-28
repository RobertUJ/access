#encoding:utf-8
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse , HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
 
from django.contrib.auth.models import User
from access.apps.citas.models import cita
from access.apps.membresias.models import membresia
from access.apps.actividades.models import actividad

from access.apps.citas.forms import frmCita,frmCitaAvion

from django.core.mail import EmailMultiAlternatives 
import json
from django.template import loader, Context
from django.conf import settings
import ast

# Funciones/Herramientas
def add_act(_miembro,texto=""):
	_texto = str(texto)
	try:
		objAct = actividad(miembro=_miembro,descripcion=_texto)
		objAct.save()
		return True
	except Exception, e:
		return False
	


def envia_email_vuelo(objCita):
	to_mem_dos = ""
	try:
		idMiembro = objCita.miembro.id
		objMiembro = get_object_or_404(User,pk=idMiembro)
		to_mem = objMiembro.email
		subject = "24 Access | Información de Vuelo"
		html_content = "Para poder aprobar su solicitud de cita para consulta con fecha %s, es necesario llenar los datos del vuelo <br><br> Aquí puede modificar la información requerida <a href=''>http:/url/cita/info_vuelo</a>" % objCita.fecha_cita
		msg = EmailMultiAlternatives(subject,html_content,'from@server.com',[to_mem])
		msg.attach_alternative(html_content,'text/html') #Definimos el contenido como HTML
		msg.send() #enviamos el correo	
		return True
	except:
		return False

@login_required(login_url='/usuarios/login/')
def citas(request):
	user_type = int(request.user.profile.tipo_usuario)
	if user_type == 4:
		if request.method == "POST":
			objCita = cita.objects.all().order_by('-estado','fecha_cita','-confirmada')
		else:
			objCita = cita.objects.all().order_by('-estado','fecha_cita','-confirmada')
		ctx = {'citas':objCita}
		return render_to_response('citas/citas_admin.html',ctx,context_instance=RequestContext(request))
	else:
		objCita = cita.objects.filter(miembro=request.user).order_by('-estado','fecha_cita','-confirmada')
		ctx = {'citas':objCita}
		return render_to_response('citas/citas.html',ctx,context_instance=RequestContext(request))

@login_required
def citas_filtros_all(request):
	objCitas = cita.objects.all()
	t = loader.get_template('citas/cita_template.html')
	c = Context({'citas':objCitas,'STATIC_URL':settings.STATIC_URL})
	rendered = t.render(c)
	return HttpResponse(rendered)

@login_required
def citas_filtros(request):
	if request.method == "POST":
		_confirmadas =  request.POST.get('confirmadas','_none')
		_canceladas  =  request.POST.get('activas','_none')
		# _info_vuelo  =  request.POST.get('info_vuelo','_none')

		filtros = "{"
		if _confirmadas != '_none':
			if _confirmadas == "SI":
				filtros +=  "'confirmada':True,"
			else:
				filtros +=  "'confirmada':False,"
		
		if _canceladas != '_none':
			if _canceladas == "SI":
				filtros +=  "'estado':True,"
			else:
				filtros +=  "'estado':False,"
		
		# if _info_vuelo != '_none':
		# 	if _info_vuelo == "NO":
		# 		filtros +=  "'info_vuelo':''"
		filtros += "}"		

		filtros_ = ast.literal_eval(filtros)

		_info_vuelo = "NO"
		if filtros == "":
			objCitas = cita.objects.all()
		else:
			if _info_vuelo == "SI":
				objCitas = cita.objects.filter(**filtros_)
			else:
				objCitas = cita.objects.filter(**filtros_)



		print objCitas

		t = loader.get_template('citas/cita_template.html')
		c = Context({'citas':objCitas,'STATIC_URL':settings.STATIC_URL})
		rendered = t.render(c)

		return HttpResponse(rendered)
	else:
		return HttpResponse("test")


@login_required(login_url='/usuarios/login/')
def edita_citas(request,id_cita):
	idCita = int(id_cita)
	objCita = get_object_or_404(cita,pk=idCita)
	if request.method == "POST":
		frm = frmCita(request.POST,instance=objCita)
		if frm.is_valid():
			objCita = frm.save()
			# Agrega actividad
			texto = "Se ha modificado la solicitud de cita para la fecha %s" % objCita.fecha_cita	
			add_act(request.user,texto)
			return HttpResponseRedirect('/citas/')
		ctx ={'form':frm,'editar':True}
	else:
		ctx = {'form':frmCita(instance=objCita), 'editar':True }
	return render_to_response('citas/nueva_cita.html',ctx,context_instance=RequestContext(request))


@login_required(login_url='/usuarios/login/')
def edita_vuelo(request,id_cita):
	idCita = int(id_cita)
	objCita = get_object_or_404(cita,pk=idCita)
	if request.method == 'POST':
		frm = frmCitaAvion(request.POST,instance=objCita)
		if frm.is_valid():
			frm.save()
			# Registra actividad 
			texto = "Se ha editado la información de vuelo para la cita solicidata para la fecha %s" % objCita.fecha_cita	
			add_act(request.user,texto)
			return HttpResponseRedirect('/citas/')
		ctx ={'form':frm}
	else:
		ctx ={'form':frmCitaAvion(instance=objCita)}
	return render_to_response('citas/edita_vuelo.html',ctx,context_instance=RequestContext(request))


@login_required(login_url='/usuarios/login/')
def ver_todas_citas(request):
	ids = request.session.get('ids_citas',0)
	objCitas = cita.objects.filter(pk__in=ids)
	ctx = {'citas':objCitas}
	return render_to_response('citas/todas_citas.html',ctx,context_instance=RequestContext(request))


@login_required(login_url='/usuarios/login/')
def ver_una_cita(request,id_cita):
	idCita = int(id_cita)
	objCita = get_object_or_404(cita,pk=idCita)
	if objCita.miembro != request.user and int(request.user.profile.tipo_usuario) != 4:
		return HttpResponseRedirect('/citas/')
	ctx = {'cita':objCita}
	return render_to_response('citas/cita.html',ctx,context_instance=RequestContext(request))



@login_required
def confirma_cita(request,id_cita):
	user_type = int(request.user.profile.tipo_usuario)
	idCita = int(id_cita)
	if user_type == 4:
		objCita = get_object_or_404(cita,pk=idCita)
		objCita.confirmada = True
		objCita.save()
		
		# Registra actividad
		texto = "Felicidades, se ha confirmado la cita que solicito para la fecha %s" % objCita.fecha_cita	
		add_act(objCita.miembro,texto)

		envia_email_confirmacion(objCita)
		# Enviar a vista de mensaje de confirmacion
		return HttpResponseRedirect('/citas/')
	else:
		return HttpResponseRedirect('/citas/')


@login_required(login_url='/usuarios/login/')
def accion_citas(request):
	if request.method == "POST":
		accion = request.POST.get('accion')
		if accion == 'del':
			ids = request.POST.getlist('id_cita')
			user_type = int(request.user.profile.tipo_usuario)
			for x in ids:
				_objCita = get_object_or_404(cita,pk=x)
				texto = "Se ha eliminado la solicitud de la cita para la fecha %s" % _objCita.fecha_cita
				add_act(_objCita.miembro,texto)

			if user_type == 4:
				cita.objects.filter(pk__in=ids).delete()
			else:
				cita.objects.filter(miembro=request.user,pk__in=ids).delete()
			return HttpResponseRedirect("/citas/")

		elif accion == 'edit':
			ids_citas = request.POST.getlist('id_cita')
			if len(ids_citas) > 1:
				return HttpResponseRedirect('/citas/')
			else:
				return HttpResponseRedirect("/citas.editar/%s" % int(ids_citas[0]))
		elif accion == 'look':
			ids_citas = request.POST.getlist('id_cita')
			request.session['ids_citas'] = ids_citas
			return HttpResponseRedirect("/citas.ver/")
		elif accion == 'conf':
			user_type = int(request.user.profile.tipo_usuario)
			if user_type == 4:
				ids_citas = request.POST.getlist('id_cita')
				for x in ids_citas:
					_objCita = get_object_or_404(cita,pk=x)
					texto = "Felicidades se ha confirmado la cita que solicito para la fecha %s" % _objCita.fecha_cita
					add_act(_objCita.miembro,texto)

				if len(ids_citas) > 1:
					return HttpResponseRedirect('/citas/')
				else:
					objCita = get_object_or_404(cita,pk=ids_citas[0])
					objCita.confirmada = True
					objCita.save()
					envia_email_confirmacion(objCita)
					# Pendiente
					# Enviar a vista de mensaje de confirmacion
					return HttpResponseRedirect('/citas/')
			else:
				return HttpResponseRedirect('/citas/')
		elif accion == 'vuelo':
			user_type = int(request.user.profile.tipo_usuario)
			if user_type == 4:
				ids_citas = request.POST.getlist('id_cita')
				
				for x in ids_citas:
					_objCita = get_object_or_404(cita,pk=x)
					texto = "Un administrador ha solicidtado que llene la información del vuelo para la cita solicitada para la fecha %s" % _objCita.fecha_cita
					add_act(_objCita.miembro,texto)

				if len(ids_citas) > 1:
					objCitas = cita.objects.filter(pk__in=ids_citas)
					for c in objCitas:
						envia_email_vuelo(c)
					return HttpResponseRedirect('/citas/')
				else:
					objCitas = get_object_or_404(cita,pk=ids_citas[0])
					envia_email_vuelo(objCitas)
					return HttpResponseRedirect('/citas/')
			else:
				return HttpResponseRedirect('/citas/')


		else:
			return HttpResponseRedirect("/citas/")
	else:
		return HttpResponseRedirect("/citas/")



def envia_email_confirmacion(objCita):
	to_mem_dos = ""
	try:
		idMiembro = objCita.miembro.id
		print idMiembro
		objMiembro = get_object_or_404(User,pk=idMiembro)
		to_mem = objMiembro.email
		subject = "24 Access Membresia"
		html_content = "Felicidades, se a confirmado su cita solicitada para la fecha %s <br><br> Aquí puede ver la información <a href=''>http:/url/cita</a>" % objCita.fecha_cita
		msg = EmailMultiAlternatives(subject,html_content,'from@server.com',[to_mem])
		msg.attach_alternative(html_content,'text/html') #Definimos el contenido como HTML
		msg.send() #enviamos el correo	
		return True
	except:
		return False

@login_required(login_url='/usuarios/login/')
def crear_cita(request):
	if request.method == "POST":
		frm = frmCita(request.POST)
		if frm.is_valid():
			try:
				objMem = membresia.objects.get(miembro=request.user)
			except:
				objMem = None
				return HttpResponseRedirect("/")
			nuevaCita = frm.save(commit=False)
			nuevaCita.no_membresia = objMem
			nuevaCita.socio = request.user
			nuevaCita.miembro = request.user
			nuevaCita.estado = True
			nuevaCita.save()

			texto = "Se ha creado una nueva solicitud de cita para la fecha %s" % nuevaCita.fecha_cita
			add_act(nuevaCita.miembro,texto)

			_envia_email_solicitud(request,nuevaCita)

			return HttpResponseRedirect('/citas/')
		ctx = {'form':frm}
	else:
		frm = frmCita()
		ctx = {'form':frm}
	return render_to_response('citas/nueva_cita.html',ctx,context_instance=RequestContext(request))


def _envia_email_solicitud(request,objCita):
	to_mem_dos = ""
	try:
		to_mem = request.user.email
		subject = "24 Access Membresia"
		html_content = "Se ha genera una nueva solicitud de cita con la siguiente fecha %s <br><br> Espere confirmación." % objCita.fecha_cita
		msg = EmailMultiAlternatives(subject,html_content,'from@server.com',[to_mem])
		msg.attach_alternative(html_content,'text/html') #Definimos el contenido como HTML
		msg.send() #enviamos el correo	
		return True
	except:
		return False

@login_required(login_url='/usuarios/login/')
def  calendario_citas(request):
	import json
	import datetime
	import time

	try:
		objCitas = cita.objects.filter(miembro=request.user)
	except Exception, e:
		objCitas = None

	if not objCitas:
		ctx = {'mensaje':"No hay citas en el calendario"}
		return render_to_response('citas/calendario.html',ctx,context_instance=RequestContext(request))
	else:
		toJson = '['
		for c in objCitas:
			if c.fecha_confirmada:
				c.fecha_confirmada += datetime.timedelta(days=1)
				ff = c.fecha_confirmada.replace(tzinfo=None)
				fs = datetime.datetime(year=1970,month=1,day=1).replace(tzinfo=None)
				f = ff - fs
				# total_seconds()
				toJson += '{"date":"%s000","type":"confirmada","title":"Cita Confirmada","description":"%s","url":"/citas.ver/%s"},' % (int(round(f.total_seconds())),c.motivos_cita,c.id)
			else:
				c.fecha_cita += datetime.timedelta(days=1)
				ff = datetime.datetime(*(c.fecha_cita.timetuple()[:6])) 
				fs = datetime.datetime(year=1970,month=1,day=1).replace(tzinfo=None)
				f = ff - fs
				# total_seconds()
				toJson += '{"date":"%s000","type":"SinConfirmar","title":"Cita No Confirmada","description":"%s","url":"/citas.ver/%s"},' % (int(round(f.total_seconds())),c.motivos_cita,c.id)
		toJson += ']'

	ctx = {'mijson':toJson}
	return render_to_response('citas/calendario.html',ctx, context_instance=RequestContext(request))
