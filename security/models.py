#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User, UserManager, Group
from django.contrib.sessions.models import Session
from django.utils.encoding import smart_str

class Usuario(User):
	dni = models.CharField(max_length = 250, verbose_name = "Address", help_text = "Enter dni.", null = False, blank = False)
	phone = models.CharField(max_length = 250, verbose_name = "Phone", help_text = "Enter phone.", null = False, blank = False, default = "")
	operador = models.CharField(max_length = 250, verbose_name = "Phone", help_text = "Enter operador.", null = False, blank = False, default = "")
	objects = UserManager()

	def __unicode__(self):
		return  u'%s' % (self.username)

	def get_Full_name(self):
		return smart_str(self.last_name + " " + self.first_name)

	def get_Grupos(self):
		grupos = ""
		for x in self.groups.all():
			grupos += ", "+str(x.name)
		return u'%s' % (grupos[2:len(grupos)])

	def get_Pseudo(self):
		if self.first_name and self.last_name:
			return (self.first_name[0] + self.last_name.split(" ")[0])
		else:
			return self.first_name + " " + self.last_name

	def get_nombres(self):
		return smart_str(self.last_name + " " + self.first_name)

	def get_active_check(self):
		if self.is_active:
			return "checked"
		else:
			return ""

	def get_token(self):
		q = Token.objects.filter(usuario=self)
		if q:
			return q[0]
		else:
			return []

	def has_token(self):
		q = Token.objects.filter(usuario=self)
		if q:
			return True
		else:
			return False

class Token(models.Model):
	usuario = models.ForeignKey(Usuario, verbose_name = "Usuario", null = False, blank = False)
	frase = models.CharField(max_length = 20, verbose_name = "Frase", help_text = "Enter frase.", null = False, blank = False, default = "")

	class Meta:
		verbose_name = "Token"
		verbose_name_plural = "Tokens"

	def __str__(self):
		return self.usuario.get_Full_name()
