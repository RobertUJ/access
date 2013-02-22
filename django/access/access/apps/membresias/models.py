#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User
from django import forms


class tipo_poliza(models.Model):
	tipo_poliza = models.CharField(max_length=150,verbose_name="Tipo de póliza")

	def __unicode__(self):
		return "%s" %self.tipo_poliza

	class Meta:
		verbose_name = "Tipo de Póliza"
		verbose_name_plural = "Tipos de Pólizas"

class tipo_cobertura(models.Model):
	cobertura = models.CharField(max_length=150,verbose_name="Tipo de cobertura")

	def __unicode__(self):
		return "%s" %self.cobertura

	class Meta:
		verbose_name = "Tipo de cobertura"
		verbose_name_plural = "Tipos de Coberturas"

	
class membresia(models.Model):
	''' Modelo para los diferentes tipos de membresia que tendra el sistema  [Individual,Familiar,Corporativo]'''
	membresia_tipo  = (("1","Personal"),("3","Corporativa"),)	
	sexo_tipo 		= (("Femenino","Femenino"),("Masculino","Masculino"),)
	''' Estos son los campos para la compra de la membresia '''
	tipo					= models.CharField(max_length=50,choices=membresia_tipo)
	
	nombre 					= models.CharField(verbose_name='Nombre(s)', max_length=100)
	apellido_paterno 		= models.CharField(verbose_name='Apellido Paterno', max_length=100)
	apellido_materno 	 	= models.CharField(verbose_name="Apellido Materno", max_length=255)

	calle  					= models.CharField(verbose_name='Calle',max_length=100)
	no_exterior				= models.CharField(verbose_name="No. Exterior",max_length=10)
	no_interior	 			= models.CharField(verbose_name='No. Interior',max_length=10,blank=True,null=True)
	colonia					= models.CharField(verbose_name='Colonia',max_length=100)
	municipio				= models.CharField(verbose_name='Delegación o Municipio',max_length=150)
	ciudad					= models.CharField(verbose_name='Ciudad',max_length=100)
	cp 						= models.IntegerField(verbose_name='CP.')
	pais 					= models.CharField(verbose_name='País',max_length=150)
	
	email 					= models.EmailField(verbose_name='Email principal',max_length=200)
	re_email 		 		= models.EmailField(verbose_name='Confirma tu Mail',max_length=200,null=True,blank=True)
	
	area                    = models.CharField(verbose_name="Área internacinal",max_length=20)
	lada				    = models.CharField(verbose_name='Clave Lada',max_length=20)
	telefono				= models.CharField(verbose_name='Telefono',max_length=20)

	''' Enlace a Miembro y Call Center '''
	call_center 			= models.ForeignKey(User,related_name='CallCenter',null=True,blank=True)
	miembro 	 			= models.ForeignKey(User,related_name='Miembro',null=True,blank=True)

	''' '''
	password 				= models.CharField(verbose_name='Contraseña',max_length=250)
	renovo_pass 			= models.BooleanField(default=False)
	online 					= models.BooleanField(default=False)

	fecha_registro			= models.DateTimeField(auto_now_add=True)
	fecha_envio				= models.DateField(null=True,blank=True)
	fecha_recibo			= models.DateField(null=True,blank=True)
	activa 				    = models.BooleanField(default=False)
	pagada 					= models.BooleanField(default=False)
	activa_paquete  		= models.BooleanField(default=False)

	class Meta:
		verbose_name = 'membresia'
		verbose_name_plural = 'membresias'
		
	def __unicode__(self):
		return "%s"%(self.id) 

class MenoresEdad(models.Model):
	titular          = models.ForeignKey(User,related_name="Titulares")
	mem_titular      = models.ForeignKey(membresia,related_name="MemTitulares")
	nombre           = models.CharField(max_length=150,verbose_name="Nombre")
	apellido_paterno = models.CharField(max_length=150,verbose_name="Apellido Paterno")
	apellido_materno = models.CharField(max_length=150,verbose_name="Apellido Materno")
	fecha_nacimiento = models.DateField(verbose_name="Fecha de nacimiento")
	relacion 		 = models.CharField(max_length=100,verbose_name="Relación con el titular")
	class Meta:
		verbose_name = 'Menor de edad'
		verbose_name_plural = 'Menores de edad'

	def __unicode__(self):
		return ("%s %s %s")%(self.nombre, self.apellido_materno,self.apellido_paterno)

class PaseMenor(models.Model):
	titular 		= models.ForeignKey(User,related_name='PasesTitulares')
	menor   		= models.ForeignKey(MenoresEdad,related_name='Pases',verbose_name="Seleccione el menor de edad")
	fecha_inicio    = models.DateField() 
	fecha_fin   	= models.DateField() 
	
	def __unicode__(self):
		return ("%s %s %s")%(self.menor.nombre, self.menor.apellido_materno,self.menor.apellido_paterno)


class rel_mem(models.Model):
	titular      = models.ForeignKey(User,related_name="Usuario Titular")
	mem_titular  = models.ForeignKey(membresia,related_name="Membresia Titular")
	mem_referido = models.ForeignKey(membresia,related_name="Membresia Referida")
	fecha_hora   = models.DateTimeField(auto_now_add=True)
	
	def __unicode__(self):
		return "%s %s -- %s" % (self.titular.first_name,self.titular.last_name,self.mem_referido)
	class Meta:
		verbose_name        = "Referidos Membresia"
		verbose_name_plural = "Sistema de Referidos"




class info_adicional(models.Model):
	''' Información requerida para la activación de las membresias. '''
	membresia 				= models.ForeignKey(membresia)
	
	compania_seguros	 	= models.CharField(max_length=255,verbose_name="Compañia de seguros")
	# Se quito direccion de compañia
	# direccion_compania	 	= models.TextField(blank=True,null=True,verbose_name="Dirección de la compañía de seguros")
	nombre_representante 	= models.CharField(max_length=255,verbose_name="Nombre del representante de compañía de seguros o intermediario",blank=True,null=True)
	telefono_representante 	= models.CharField(max_length=255,verbose_name="Telefono del representante de compañía de seguros",blank=True,null=True)
	 
	# Informacion de póliza
	poliza 					= models.CharField(max_length=255,verbose_name="Póliza")
	tipo_poliza 			= models.ForeignKey(tipo_poliza, verbose_name="Selecciona el tipo de póliza")
	tipo_cobertura 			= models.ForeignKey(tipo_cobertura, verbose_name="Selecciona el tipo de cobertura")
	# Se mostraran solo si selecionan la plabra otros dentro de los select anteriores
	tipo_poliza_otro 			= models.CharField(max_length=255,verbose_name="Tipo Póliza",blank=True,null=True)
	tipo_cobertura_otro 		= models.CharField(max_length=255,verbose_name="Tipo Cobertura | Plan",blank=True,null=True)
	fecha_vencimiento           = models.DateField(verbose_name="Fecha de Vencimiento")

	# Preguntar si son requeridos estos campos
	contacto_emergencia_usa  = models.CharField(max_length=255,verbose_name='Contacto de emergencia en USA',blank=True,null=True)
	telefono_contacto_usa    = models.CharField(verbose_name='Telefono del contacto en USA', max_length=50,blank=True,null=True)
	nombre_dr_mexico	     = models.CharField(verbose_name='Nombre de tu doctor en México', max_length=255,blank=True,null=True)
	telefono_dr_mexico	     = models.CharField(verbose_name='Teléfono de tu doctor en México', max_length=255,blank=True,null=True)
	info_adicional_tx_center = models.TextField(verbose_name='Información adicional solicitada por TX Medical Center',blank=True,null=True)

	# Tiene pasaporte, si no, esconde campos y no son requeridos
		# Se elemino la pregunta si tiene pasaporte o no.
	# tiene_pasaporte         = models.BooleanField(verbose_name="¿Tiene pasaporte?")
	no_pasaporte  		    = models.CharField(verbose_name='No. Pasaporte', max_length=255,blank=True,null=True)
		# vencimiento_pasaporte   = models.DateField(verbose_name='Fecha de vencimiento del pasaporte',blank=True,null=True)
	# Tiene visa? si no, oculta campos siguientes
	# tiene_visa  		    = models.BooleanField(verbose_name='¿Tiene VISA?', max_length=255)
	no_visa					= models.CharField(verbose_name='No. VISA', max_length=255,blank=True,null=True)
	# vencimiento_visa   		= models.DateField(verbose_name='Fecha de vencimiento de la VISA',blank=True,null=True)
	class Meta:
		verbose_name = 'Info. adicional para activación'
		verbose_name_plural = 'Información Adicional'
	
	def __unicode__(self):
		return "%s" %self.compania_seguros
    

class miembros_adicionales(models.Model):
	''' Modelo para la relación de miembros adicionales de cada titular de membresias '''
	sexo_tipo = (("Femenino","Femenino"),("Masculino","Masculino"),)

	membresia 			 	= models.ForeignKey(membresia,verbose_name="Seleccione la membresia",blank=True,null=True)

	nombre				 	= models.CharField(max_length=255,verbose_name="Nombre (s)")
	apellido_paterno 	 	= models.CharField(verbose_name="Apellido Paterno", max_length=255)
	apellido_materno 	 	= models.CharField(verbose_name="Apellido Materno", max_length=255)
	genero 				 	= models.CharField(verbose_name="Género", choices=sexo_tipo, max_length=10)
	nacionalidad		 	= models.CharField(max_length=100)
	fecha_nacimiento       	= models.DateField(verbose_name="Fecha de Nacimiento")
	parentesco			 	= models.CharField(max_length=255,verbose_name="¿Cúal es el parentesco con el titular de la membresia?")

	# Comparte Poliza? Si es False se muestran la info de captura de poliza.
	comparte_poliza      	= models.BooleanField(default=False)
	
	# Informacion del intermediario
	nombre_representante 	= models.CharField(max_length=255,verbose_name="Nombre del representante de compañía de seguros o intermediario",blank=True,null=True)
	telefono_representante 	= models.CharField(max_length=255,verbose_name="Telefono del representante de compañía de seguros",blank=True,null=True)
	# Información de póliza
	poliza 					= models.CharField(max_length=255,verbose_name="Póliza",blank=True,null=True)
	tipo_poliza 			= models.ForeignKey(tipo_poliza, verbose_name="Seleccione el tipo de póliza",blank=True,null=True)
	tipo_cobertura 			= models.ForeignKey(tipo_cobertura, verbose_name="Seleccione el tipo de cobertura",blank=True,null=True)
	# Se mostraran solo si selecionan la plabra otros dentro de los select anteriores
	tipo_poliza_otro 			= models.CharField(max_length=255,verbose_name="Tipo Póliza",blank=True,null=True)
	tipo_cobertura_otro 		= models.CharField(max_length=255,verbose_name="Tipo Cobertura | Plan",blank=True,null=True)
	fecha_vencimiento       = models.DateField(verbose_name="Fecha Vencimiento",blank=True,null=True)

	no_pasaporte  		    = models.CharField(verbose_name='No. Pasaporte', max_length=255,blank=True,null=True)
	no_visa					= models.CharField(verbose_name='No. VISA', max_length=255,blank=True,null=True)

	class Meta:
		verbose_name = 'Miembro adicional'
		verbose_name_plural = 'Miembros adicionales'
	def __unicode__(self):
		return "%s %s %s" %(self.nombre,self.apellido_paterno,self.apellido_materno)
    


