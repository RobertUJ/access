#encoding:utf-8
from django import forms
from django.db import models
from django.forms import ModelForm
from access.apps.membresias.models import membresia,info_adicional,MenoresEdad,PaseMenor
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
		fields = ['tipo', 'nombre','apellido_paterno','apellido_materno','email','re_email',]
		# exclude = [ 'call_center','miembro','password','online','renovo_pass','fecha_registro','fecha_envio','fecha_recibo','activa','activa_paquete',]

class frmCantidad(forms.Form):
	cantidad = forms.IntegerField(
		label='Cantidad de membresias a comprar',
		required=True)
		
		



class frmComMem(forms.ModelForm):
	nombre = forms.CharField(
		widget=forms.TextInput(
			attrs={'class':'input-medium',}
		),
		label='Nombre(s):',
	)
	apellido_paterno = forms.CharField(
		widget=forms.TextInput(
			attrs={'class':'input-medium',}
		),
		label='Apellido Paterno:',
	)
	apellido_materno = forms.CharField(
		widget=forms.TextInput(
			attrs={'class':'input-medium',}
		),
		label='Apellido Materno:',
	)
	email = forms.EmailField(
		widget=forms.TextInput(
			attrs={'class':'input-medium',}
		),
		label='Email:',
	)
	re_email = forms.EmailField(
		widget=forms.TextInput(
			attrs={'class':'input-medium',}
		),
		label='Re-Ingresa tu email:',
	)
	
	def __init__(self, *arg, **kwarg):
		super(frmComMem, self).__init__(*arg, **kwarg)
		self.empty_permitted = False

	def clean(self):
		''' Required custom validation for the form. '''
		super(frmComMem,self).clean()
		if 'email' in self.cleaned_data and 're_email' in self.cleaned_data:
			if self.cleaned_data.get('email') != self.cleaned_data.get('re_email'):
				self._errors['email'] = self.error_class([u'Los campos de correos electrónico deben coincidir.'])
				self._errors['re_email'] = self.error_class([u'Los campos de correos electrónico deben coincidir.'])
		return self.cleaned_data

	class Meta:
		model = membresia
		fields = ['nombre','apellido_paterno','apellido_materno','email','re_email',]
		# exclude = [ 'call_center','miembro','password','online','renovo_pass','fecha_registro','fecha_envio','fecha_recibo','activa','activa_paquete',]


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
		model = MenoresEdad
		exclude =['titular','mem_titular','relacion']

class frmPaseMenor(forms.ModelForm):
	class Meta:
		model = PaseMenor
		exclude = ['titular','fecha_inicio','fecha_fin']

class frmCompraMembresiaOnline(forms.ModelForm):
	class Meta:
		model = membresia
		exclude = ['call_center','miembro','renovo_pass','online','fecha_registro','fecha_envio','fecha_recibo','activa','activa_paquete',]

class frmActivaMembresia(forms.Form):
	membresia 	= forms.CharField(widget=forms.TextInput())
	password 	= forms.CharField(widget=forms.PasswordInput())


class frmActualizaMembresia(forms.ModelForm):
	class Meta:
		model = membresia
		exclude = ['tipo','call_center','miembro','password','renovo_pass','online','fecha_registro','fecha_envio','fecha_recibo','activa','pagada','activa_paquete']


class frmInfoActivacion(forms.ModelForm):
	class Meta:
		model = info_adicional
		exclude = ['membresia',]


def validate_username_unique(value):
	''' Custom validator for user uniqueness. '''
	if User.objects.filter(username=value).exists():
		raise ValidationError(u'El nombre de usuario "%s" ya existe. ' % value)


class UserEditForm(ModelForm):
    class meta:
        model = User
 
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(UserEditForm, self).__init__(*args, **kwargs)
    



class editUserFrm(forms.Form):
	username	=	forms.CharField(
		max_length=20,
		widget=forms.TextInput(
			attrs={'class':'','placeholder':'','readonly':'readonly'},
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
