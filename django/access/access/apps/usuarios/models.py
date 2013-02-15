#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.db.models.signals import post_save

""" Selectores para el registro """	
cho_type = (("1","Cliente"),("2","Cliente - Corporativo"),("3","Call Center"),("4","Admin"))
genero_tipo = (("M","Mujer"),("2","Hombre"))
estado_civil_tipo = (("Soltero","Soltero"),("Casado","Casado"),("Union Libre","Union Libre"),("Divorciado","Divorciado"),("Viudo","Viuda"))
no_hijos = (("1","1"),("2","2"),("3","3"),("4","4"),("5","5"),("6","6"),("7","7"),("8","8"),("9","9"),("10","10"))

class UserProfile(models.Model):
	user				= models.ForeignKey(User,unique = True)
	tipo_usuario		= models.CharField(max_length=2,default="1", choices=cho_type,null=True,blank=True)
	genero				= models.CharField(max_length=1,choices=genero_tipo,verbose_name="Género",null=True,blank=True)
	fecha_nacimiento	= models.DateField(verbose_name="Fecha de nacimiento",null=True,blank=True)
	estado_civil		= models.CharField(max_length=20,choices=estado_civil_tipo,verbose_name="Estado civil",null=True,blank=True)
	hijos_menores_edad	= models.CharField(max_length=5, choices=no_hijos,verbose_name="No. de hijos menores de 18 años",null=True,blank=True)
	calle 				= models.CharField(max_length=255,verbose_name="Calle",null=True,blank=True)
	no_exterior			= models.CharField(max_length=10,verbose_name="No. Exterior",null=True,blank=True)
	no_interior			= models.CharField(max_length=10,verbose_name="No. Interior",null=True,blank=True)
	colonia				= models.CharField(max_length=100,verbose_name="Colonia",null=True,blank=True)
	municipio			= models.CharField(max_length=150,verbose_name="Delegación y Municipio",null=True,blank=True)
	ciudad				= models.CharField(max_length=150,verbose_name="Ciudad",null=True,blank=True)
	estado 				= models.CharField(max_length=150,verbose_name="Estado",null=True,blank=True)
	cp 					= models.IntegerField(verbose_name="CP",null=True,blank=True)
	telefono 			= models.CharField(max_length=150,verbose_name="Teléfono",null=True,blank=True)
	membresia_activa	= models.BooleanField(default=False)

	def __unicode__(self):
		_user = self.user
		if _user.first_name == "" and _user.last_name == "":
			return "%s" % _user.username
		else:
			return "%s %s" %(_user.first_name,_user.last_name)

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

def create_user_profile(sender,instance,created, **kwargs):
	if created:
	    UserProfile.objects.create(user=instance)
post_save.connect(create_user_profile,sender=User)
