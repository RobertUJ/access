#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User
from django import forms
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
	''' Modelo para la creación de citas '''
	# Relacionarla con datos de contacto y  problemas
	no_membresia			= models.ForeignKey(membresia)

	es_titular 				= models.BooleanField(default=False,verbose_name='¿Es el titular de la membresía?')
	
	relacion_titular 		= models.CharField(max_length=255,null=True,blank=True,verbose_name='¿Cuál es la relación con el titular de la membresía?')
	nombre_completo			= models.CharField(max_length=255,null=True,blank=True,verbose_name='Nombre completo de quién solicita la cita')
	datos_contacto			= models.TextField(null=True,blank=True,verbose_name='Datos de contacto, de quién solicita la cita')
		
	fecha_cita				= models.DateField(null=False,blank=False,verbose_name='Fecha aproximada de la cita')
	preferencia_horario 	= (("Manana","Mañana"),("Tarde","Tarde"),)
	preferencia				= models.CharField(max_length=50,choices=preferencia_horario,verbose_name="Preferencia de horario")

	especialidad_cita		= models.ForeignKey(especialidad,verbose_name='Especialidad para la cita',help_text="Si no conoces tu especialidad selecciona medicina interna.")
	especialidad_cita_otra	= models.CharField(max_length=255,verbose_name='Agregue la otra especialidad.',null=True,blank=True)
	motivos_cita			= models.TextField(null=True,blank=True,verbose_name='Motivos de tu cita',help_text="Ser tan amplio como puedas")
	
	estudios_fechas			= models.TextField(null=True,blank=True,verbose_name='Si tiene estudios previos, mencione cuales y en que fecha se revisaron')

	uso_poliza				= models.BooleanField(default=False,verbose_name='¿Harás uso de tu póliza de seguro? (Le recomendamos llenar los formularios que hablan de su póliza)')
	recomendaciones			= models.BooleanField(default=False, verbose_name = "¿Has leido las recomendaciones?")

	atendido_huston			= models.BooleanField(default=False,verbose_name='¿Ha recibido alguna vez tratamiento o atencion medica en el TMC?')
	donde					= models.CharField(max_length=255,verbose_name='¿En donde te atendieron?',null=True,blank=True)
	cuando					= models.DateField(verbose_name='¿En que fecha te atendieron?',null=True,blank=True)

	comentarios 			= models.TextField(verbose_name='Comentarios adicionales',null=True,blank=True)
	
	confirmada				= models.BooleanField(default=False)
	fecha_confirmada 		= models.DateTimeField(null=True,blank=True,verbose_name='Fecha y Hora confirmada para la cita en Houston')
	conf_miembro 			= models.BooleanField(default=False)

	fecha_hora 				= models.DateTimeField(auto_now_add=True)
	estado					= models.BooleanField(default=False)

	socio     				= models.ForeignKey(User,related_name="Socio",null=True,blank=True)
	miembro   				= models.ForeignKey(User,related_name="Membresia",null=True,blank=True)

	class Meta:
		verbose_name = 'Cita'
		verbose_name_plural = 'Citas'
	
	def __unicode__(self):
		return "Fecha Solicitada %s" % self.fecha_cita



class Vuelo(models.Model):
	Cita = models.ForeignKey(cita,related_name="citas",unique=True)
	HoraFecha = models.DateTimeField(verbose_name="Fecha y Hora")
	Aerolinea = models.CharField(max_length=100)
	Vuelo = models.CharField(max_length=100,verbose_name="Numero de Vuelo")
	Comentarios = models.TextField(verbose_name="Comentarios adicionales")
	Estado 	= models.BooleanField(default=False)
    
	class Meta:
	    verbose_name = 'vuelo'
	    verbose_name_plural = 'vuelos'

	def __unicode__(self):
	    return "%s" % self.Cita 
    



		

	


