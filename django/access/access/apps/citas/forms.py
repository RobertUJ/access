#encoding:utf-8

from django import forms
from django.forms import ModelForm
from django.db import models
from django.forms import ModelChoiceField
from access.apps.citas.models import cita



class frmCita(forms.ModelForm):
	class Meta:
		model = cita
		exclude = ['recomendaciones','no_membresia','confirmada','socio','miembro','estado','fecha_confirmada']


class frmCitaAvion(forms.ModelForm):
	class Meta:
		model = cita
		fields = ['recomendaciones',]
