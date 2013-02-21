#encoding:utf-8
from django import forms
from django.db import models
from django.forms import ModelForm
from access.apps.membresias.models import membresia,info_adicional,menores_edad,pase_menor
from django.contrib.auth.models import User
from django.forms import ModelChoiceField
from django.core import validators
from django.core.exceptions import ValidationError

class frmCompraMembresiaCallCenter(forms.ModelForm):
	def clean(self):
		''' Required custom validation for the form. '''
		super(ModelForm,self).clean()
		if 'email' in self.cleaned_data and 're_email' in self.cleaned_data:
			if self.cleaned_data.get('email') != self.cleaned_data.get('re_email'):
				self._errors['email'] = self.error_class([u'Los campos de correos electrónico deben coincidir.'])
				self._errors['re_email'] = self.error_class([u'Los campos de correos electrónico deben coincidir.'])
		return self.cleaned_data

	class Meta:
		model = membresia
		exclude = ['call_center','miembro','password','online','renovo_pass','fecha_registro','fecha_envio','fecha_recibo','activa','activa_paquete',]


class frmCompraAdicional(forms.ModelForm):
	def clean(self):
		''' Required custom validation for the form. '''
		super(ModelForm,self).clean()
		if 'email' in self.cleaned_data and 're_email' in self.cleaned_data:
			if self.cleaned_data.get('email') != self.cleaned_data.get('re_email'):
				self._errors['email'] = self.error_class([u'Los campos de correos electrónico deben coincidir.'])
				self._errors['re_email'] = self.error_class([u'Los campos de correos electrónico deben coincidir.'])
		return self.cleaned_data

	class Meta:
		model = membresia
		exclude = ['call_center','miembro','password','online','renovo_pass','fecha_registro','fecha_envio','fecha_recibo','activa','activa_paquete',]




		
class frmMenoresEdad(forms.ModelForm):
	class Meta:
		model = menores_edad
		exclude =['titular','mem_titular',]

class frmPaseMenor(forms.ModelForm):
	class Meta:
		model = pase_menor
		exclude = ['titular',]




class frmCompraMembresiaOnline(forms.ModelForm):
	class Meta:
		model = membresia
		exclude = ['call_center','miembro','renovo_pass','online','fecha_registro','fecha_envio','fecha_recibo','activa','activa_paquete',]

class frmActivaMembresia(forms.Form):
	membresia 	= forms.CharField(widget=forms.TextInput())
	password 	= forms.CharField(widget=forms.PasswordInput())


class frmInfoActivacion(forms.ModelForm):
	class Meta:
		model = info_adicional
		exclude = ['membresia',]


def validate_username_unique(value):
	''' Custom validator for user uniqueness. '''
	if User.objects.filter(username=value).exists():
		raise ValidationError(u'El nombre de usuario "%s" ya existe. ' % value)



class registerUserFrm(forms.Form):
	username	=	forms.CharField(
		max_length=20,
		widget=forms.TextInput(
			attrs={'class':'','placeholder':''},
		),
		required=True,
		min_length=4,
		validators=[validate_username_unique],
		label="Crea tu Usuario",
	)
	password 	= 	forms.CharField(
		max_length=20,
		min_length=4,
		widget=forms.PasswordInput(
			attrs={'class':'','placeholder':''},
		),
		required=True,
		label="Crea tu Contraseña",
	)
	repassword 	= 	forms.CharField(
		max_length=20,
		min_length=4,
		widget=forms.PasswordInput(
			attrs={'class':'','placeholder':''},
		),
		required=True,
		label="Confirma tu contraseña",
	)

	def clean(self):
 		''' Required custom validation for the form. '''
 		super(forms.Form,self).clean()
 		if 'password' in self.cleaned_data and 'repassword' in self.cleaned_data:
 			if self.cleaned_data['password'] != self.cleaned_data['repassword']:
 				self._errors['password'] = [u'Passwords must match.']
				self._errors['repassword'] = [u'Password must match']
		return self.cleaned_data
