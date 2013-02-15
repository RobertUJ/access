#encoding:utf-8
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse , HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
#Modelos 
from django.contrib.auth.models import User
from access.apps.actividades.models import actividad
# Formularios

# Librerias / Herramientas
from django.core.mail import EmailMultiAlternatives 

@login_required
def actividades_all(request):
	objActividades = actividad.objects.filter(miembro=request.user).order_by('-fecha')
	ctx = {"acts":objActividades}
	return render_to_response('actividades/actividades.html',ctx,context_instance=RequestContext(request))


@login_required
def ver_actividad(request,idActividad):
	idAct = int(idActividad)
	objAct = get_object_or_404(actividad,pk=idAct)
	ctx = {"act":objAct}
	return render_to_response('actividades/actividad.html',ctx,context_instance=RequestContext(request))
