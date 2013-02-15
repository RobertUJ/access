#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User
from django import forms
#from sorl.thumbnail import ImageField
# Modelos
from access.apps.membresias.models import membresia

class especialidad(models.Model):
	especialidad  = models.CharField(max_length=150,verbose_name="Especialidad")
	
	def __unicode__(self):
		return "%s" % self.especialidad
	class Meta:
		verbose_name = "Especialidad para citas"
		verbose_name_plural = "Especialidades para las citas"

class cita(models.Model):
	''' Modelo para la creación de citas  '''
	# Relacionarla con datos de contacto y  problemas
	no_membresia			= models.ForeignKey(membresia)

	es_titular 				= models.BooleanField(default=False,verbose_name='¿Es el titular de la membresía?')
	
	relacion_titular 		= models.CharField(max_length=255,null=True,blank=True,verbose_name='¿Cuál es la relación con el titular de la membresía?')
	nombre_completo			= models.CharField(max_length=255,null=True,blank=True,verbose_name='Nombre completo de quién solicita la cita')
	datos_contacto			= models.TextField(null=True,blank=True,verbose_name='Datos de contacto, de quién solicita la cita')
		
	fecha_cita				= models.DateField(null=False,blank=False,verbose_name='Fecha para la cita solicitada')
	hora_cita 				= models.TimeField(null=False,blank=False,verbose_name='Hora para la cita solicitada')
	especialidad_cita		= models.ForeignKey(especialidad,verbose_name='Especialidad para la que solicita la cita')
	especialidad_cita_otra	= models.CharField(max_length=255,verbose_name='Agregue la otra especialidad.',null=True,blank=True)
	motivos_cita			= models.TextField(null=True,blank=True,verbose_name='Motivos de la cita')
	
	estudios_fechas			= models.TextField(null=True,blank=True,verbose_name='Si le han hecho estudios, ingrese que estudios y fechas en las que se realizaron')

	uso_poliza				= models.BooleanField(default=False,verbose_name='¿Hára huso de la póliza?')
	recomendaciones			= models.BooleanField(default=False, verbose_name = "¿Ha leido las recomendaciones?")

	atendido_huston			= models.BooleanField(default=False,verbose_name='¿Lo han atendido en el Centro Médico de Huston?')
	donde					= models.CharField(max_length=255,verbose_name='¿En donde lo atendieron?',null=True,blank=True)
	cuando					= models.DateField(verbose_name='¿En que fecha lo atendieron?',null=True,blank=True)

	comentarios 			= models.TextField(verbose_name='Comentarios adicionales',null=True,blank=True)
	
	confirmada				= models.BooleanField(default=False)
	fecha_hora 				= models.DateTimeField(auto_now=True)
	estado					= models.BooleanField(default=False)

	info_vuelo				= models.TextField(verbose_name='Agregue la información del vuelo',null=True,blank=True)

	socio     				= models.ForeignKey(User,related_name="Socio",null=True,blank=True)
	miembro   				= models.ForeignKey(User,related_name="Membresía",null=True,blank=True)

	class Meta:
		verbose_name = 'Cita'
		verbose_name_plural = 'Citas'
	
	def __unicode__(self):
		return "%s" % self.fecha_cita






	


