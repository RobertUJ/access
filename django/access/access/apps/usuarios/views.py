#encoding:utf-8
from django.shortcuts import render_to_response,get_object_or_404
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
# Models
from django.contrib.auth.models import User
from access.apps.usuarios.models import UserProfile
from access.apps.usuarios.forms import frmPerfil,UserForm,LoginForm
from django.contrib.auth.forms import UserCreationForm
from django.core.mail 			import EmailMultiAlternatives 

def login_view(request):
	strMsg =""
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')
	else:
		if request.method == "POST":
			objForm = LoginForm(request.POST)
			if objForm.is_valid():
				username = objForm.cleaned_data['username']
				password = objForm.cleaned_data['password']
				objUser = authenticate(username=username,password=password)
				if objUser is not None and objUser.is_active:
					login(request,objUser)
					user_type = int(objUser.profile.tipo_usuario)
					url_redirect = ""
					if   user_type == 4:
						url_redirect = "/admin/"
					else:
						url_redirect = "/citas/"					
					return HttpResponseRedirect(url_redirect)
				else:
					strMsg = "Usuario ó contraseña incorrecto"
		objForm = LoginForm()
		ctx = {'form': objForm,'msg':strMsg}
		return render_to_response('forms/usuarios/login.html',ctx,context_instance=RequestContext(request))


def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')



def llenar_info_adicional(request):
	if request.method == "POST":
		frm = frmInfoAdicional(request.POST)
		if frm.is_valid():
			frmUncommit = frm.save(commit=False)
			frmUncommit.usuario = request.user
			frmUncommit.save()
			test = get_object_or_404(info_adicional,usuario=request.user)
			frm = frmInfoAdicional(instance=test)
			ctx = {'formAdicional':frm}
			return render_to_response('forms/usuarios/infoAdicional.html',ctx,context_instance=RequestContext(request))
		else:
			ctx = {'formAdicional':frm}
			return render_to_response('forms/usuarios/infoAdicional.html',ctx,context_instance=RequestContext(request))

	frm = frmInfoAdicional()
	ctx = {'formAdicional':frm}
	return render_to_response('forms/usuarios/infoAdicional.html',ctx,context_instance=RequestContext(request))


def registro_usuarios(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect("/")
	
	if request.method == "POST":
		createFrm 	= UserCreationForm(request.POST)
		userFrm 	= UserForm(request.POST)
		perfil  	= frmPerfil(request.POST)
		if createFrm.is_valid() and userFrm.is_valid() and perfil.is_valid():
			username_ 			= createFrm.cleaned_data['username']
			password_ 			= createFrm.cleaned_data['password1']
			email_ 				= userFrm.cleaned_data['email']
			new_user 			= User.objects.create_user(username= username_, email= email_,password=password_)
			new_user.is_staff 	= False
			new_user.first_name = userFrm.cleaned_data['first_name']
			new_user.last_name 	= userFrm.cleaned_data['last_name']
			new_user.save()
			''' Add data to UserProfile model '''
			new_profile 					= UserProfile.objects.get(user=new_user)
			new_profile.genero 				= perfil.cleaned_data['genero']
			new_profile.fecha_nacimiento 	= perfil.cleaned_data['fecha_nacimiento']
			new_profile.estado_civil 		= perfil.cleaned_data['estado_civil']
			new_profile.hijos_menores_edad 	= perfil.cleaned_data['hijos_menores_edad']
			new_profile.calle 				= perfil.cleaned_data['calle']
			new_profile.no_exterior 		= perfil.cleaned_data['no_exterior']
			new_profile.no_interior 		= perfil.cleaned_data['no_interior']
			new_profile.colonia 			= perfil.cleaned_data['colonia']
			new_profile.municipio 			= perfil.cleaned_data['municipio']
			new_profile.ciudad 				= perfil.cleaned_data['ciudad']
			new_profile.estado 				= perfil.cleaned_data['estado']
			new_profile.cp 					= perfil.cleaned_data['cp']
			new_profile.telefono 			= perfil.cleaned_data['telefono']
			new_profile.save()
			""" Envia correo para el llenado de la siguiente información"""
			to_user = email_
			subject = "Activa membresia 24access"
			html_content = "Bienvenido al sistema 24access, por favor complete la información de registro para activar su membresia <br/> <a href='http://desarrollo.servebeer.com:8888/usuarios/login/' >Click aquí</a> O bien, copie y pegue esta liga en su navegador http://desarrollo.servebeer.com:8888/usuarios/login/ "
			msg = EmailMultiAlternatives(subject,html_content,'from@server.com',[to_user])
			msg.attach_alternative(html_content,'text/html') #Definimos el contenido como HTML
			msg.send() #enviamos el correo

			return HttpResponseRedirect('/')
		else:
			ctx={"frmPer":perfil,"frmUser":userFrm,'frmCreate':createFrm}
			return render_to_response('forms/usuarios/registro.html',ctx,context_instance=RequestContext(request))

	_create    = UserCreationForm()
	_frmPerfil = frmPerfil()
	_frmUser   = UserForm()
	ctx={"frmPer":_frmPerfil,"frmUser":_frmUser,'frmCreate':_create}
	return render_to_response('forms/usuarios/registro.html',ctx,context_instance=RequestContext(request))

