from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class actividad(models.Model):
	miembro   = models.ForeignKey(User,related_name='miembros')
	descripcion = models.TextField()
	fecha     = models.DateTimeField(auto_now_add=True)
	leido     = models.BooleanField(default=False)
	def __unicode__(self):
		return "%s" % self.fecha



