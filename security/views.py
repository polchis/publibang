#encoding:utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from security.models import Usuario, Token
from security.forms import LoginForm, RegistroForm
import datetime
import time
import json
import uuid

def getAplicacion():
	return {
		'root' : '/',
		'app' : {'nombre' : 'Sistema de Información Rosa de Lima'}
	}

def hasPermission(u, patron):
	for uu in u:
		if uu.id == patron:
			return True
	return False

def isLogin(u):
	if u is not None and u.is_active:
		return True
	else:
		return False

def login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			passwd = form.cleaned_data['password']
			user = authenticate(username = username, password = passwd)
			if user is not None:
				if user.is_active:
					auth_login(request, user)
					try:
						usuario = Usuario.obejects.get(id=user.id)
						if not usuario.has_token():
							token = Token(usuario=usuario, frase=uuid.uuid4())
							token.save()
					return HttpResponseRedirect('/')
				else:
					messages.add_message(request, 50, 'Usuario inactivo.', 'error')
		else:
			messages.add_message(request, 50, 'Verifique sus datos.', 'error')
	return render_to_response('security/login.html', {}, context_instance = RequestContext(request))

def registro(request):
	if request.method == 'POST':
		POST = request.POST.copy()
		POST['is_active'] = True
		form = RegistroForm(POST)
		if form.is_valid() and POST['password']==POST['password2'] and POST['password']!="":
			nuevo_usuario = form.save()
			nuevo_usuario.set_password(form.cleaned_data['password'])
			nuevo_usuario.save()
			return HttpResponseRedirect('/')
		else:
			print form.errors
			messages.add_message(request, 50, 'Verifique sus datos.', 'error')
	else:
		form = RegistroForm()
	return render_to_response('security/registro.html', {}, context_instance = RequestContext(request))

def onlogout(request):
	if request.user != "AnonymousUser":
		logout(request)
	return HttpResponseRedirect('/')

def usuariox_pass(request, codigo):
	usuario = request.user
	if not (isLogin(usuario)):
		return HttpResponseRedirect("/login/")
	if (hasPermission(usuario.groups.all(), 1)):
		Generals = {
			'aplicacion' : getAplicacion(),
			'items' : getMenuFirst(usuario.groups.all()),
			'menu' :  getMenuSecond(usuario.groups.all()),
			'titulo' : 'Formulario de Usuarios',
			'titulo_segundo' : "Lista de Usuarios",
			'action' : '/usuario/',
			'objetos' : Usuario.objects.all().order_by('last_name'),
			'suject' : [],
		}
		if request.method == 'POST':
			if codigo:
				try:
					Generals['suject'] = Usuario.objects.get(id = codigo)
					Generals['suject'].set_password(request.POST['password'])
					Generals['suject'].save()
					messages.success(request, ("Se modificó satisfactoriamente la contraseña de " + str(Generals['suject'].username) ))
				except:
					logear(str(datetime.datetime.now()) + " - usuariox_registro" + " - Usuario.objects.get(id = codigo)")
					return HttpResponseRedirect('/404/')
			return HttpResponseRedirect('/usuario/')
		else:
			Generals['suject'] = Usuario.objects.get(id = codigo)
			Generals['action'] += "password/"
			codigo += "/"
			form = UsuarioFormPass()
			messages.info(request, ("Editando la contraseña de " + str(Generals['suject'].username) ))
			context = {
					'codigo' : codigo,
					'form' : form,
			}
		return render_to_response('security/lista.html', context, context_instance = RequestContext(request))
	return HttpResponseRedirect('/')


def ganador(request):
	return render_to_response('ganador.html', {}, context_instance = RequestContext(request))