#encoding:utf-8

from django.db import models
from security.models import Usuario
from django.conf import settings
from pytz import timezone

# Create your models here.

class Concurso(models.Model):
	nombre = models.CharField(max_length = 250, verbose_name = "Nombre", help_text = "Ingrese nombre.", null = False, blank = False)
	inicio = models.DateTimeField(verbose_name = "Fecha de inicio", help_text = "Ingrese fecha de inicio.", null = False, blank = False)
	fin = models.DateTimeField(verbose_name = "Fecha de fin", help_text = "Ingrese fecha de fin.", null = False, blank = False)
	premiacion = models.DateTimeField(verbose_name = "Fecha de premiacion", help_text = "Ingrese fecha de premiacion.", null = False, blank = False)
	estado = models.BooleanField(verbose_name = "Estado", help_text = "Check si esta activo.", default=False)

	class Meta:
		verbose_name = "Consurso"
		verbose_name_plural = "Consursos"

	def __unicode__(self):
		return self.nombre

	def get_participantes(self):
		return Participa.objects.filter(concurso=self)


class Lugar(models.Model):
	nombre = models.CharField(max_length = 250, verbose_name = "Nombre", help_text = "Ingrese nombre.", null = False, blank = False)
	estado = models.BooleanField(verbose_name = "Estado", help_text = "Check si esta activo.", default=False)

	class Meta:
		verbose_name = "Lugar"
		verbose_name_plural = "Lugares"

	def __unicode__(self):
		return self.nombre


class Participa(models.Model):
	usuario = models.ForeignKey(Usuario, verbose_name = "Usuario", null = False, blank = False)
	concurso = models.ForeignKey(Concurso, verbose_name = "Concurso", null = False, blank = False)
	lugar = models.ForeignKey(Lugar, verbose_name = "Lugar", null = True, blank = True)
	creacion = models.DateTimeField(auto_now_add = True, verbose_name="Fecha de Ingreso.", help_text = "Ingrese la Fecha de Ingreso.", null = False, blank = False)
	modificado = models.DateTimeField(auto_now = True, verbose_name="Fecha de Modificación.", help_text = "Ingrese la Fecha de Modificación.", null = False, blank = False)

	class Meta:
		verbose_name = "Participa"
		verbose_name_plural = "Participantes"

	def __unicode__(self):
		return self.usuario.get_Full_name()

	def get_creacion_text(self):
		return self.creacion.astimezone(timezone(settings.TIME_ZONE)).strftime('%d-%m-%Y %H:%M')

class TokenParticipa(models.Model):
	usuario = models.ForeignKey(Usuario, verbose_name = "Usuario", null = False, blank = False)
	frase = models.CharField(max_length = 20, verbose_name = "Frase", help_text = "Enter frase.", null = False, blank = False, default = "")
	lugar = models.ForeignKey(Lugar, verbose_name = "Lugar", null = True, blank = True)
	creacion = models.DateTimeField(auto_now_add = True, verbose_name="Fecha de Ingreso.", help_text = "Ingrese la Fecha de Ingreso.", null = False, blank = False)
	modificado = models.DateTimeField(auto_now = True, verbose_name="Fecha de Modificación.", help_text = "Ingrese la Fecha de Modificación.", null = False, blank = False)

	class Meta:
		verbose_name = "TokenParticipa"
		verbose_name_plural = "Tokens de Participa"

	def __unicode__(self):
		return self.usuario.get_Full_name()
