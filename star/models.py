#encoding:utf-8

from django.db import models
from security.models import Usuario

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


class Participa(models.Model):
	usuario = models.ForeignKey(Usuario, verbose_name = "Usuario", null = False, blank = False)
	concurso = models.ForeignKey(Concurso, verbose_name = "Concurso", null = False, blank = False)
	creacion = models.DateTimeField(auto_now_add = True, verbose_name="Fecha de Ingreso.", help_text = "Ingrese la Fecha de Ingreso.", null = False, blank = False)
	modicado = models.DateTimeField(auto_now = True, verbose_name="Fecha de Modificación.", help_text = "Ingrese la Fecha de Modificación.", null = False, blank = False)

	class Meta:
		verbose_name = "Participa"
		verbose_name_plural = "Participantes"

	def __str__(self):
		return self.usuario.get_Full_name()
