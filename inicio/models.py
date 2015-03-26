from django.db import models

class Registro(models.Model):
	usuario=models.CharField(max_length=200)

	def __unicode__(self):
		usuario=self.usuario
		return usuario
