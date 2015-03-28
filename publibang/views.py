#encoding:utf-8

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings
from star.models import Concurso, Participa
from security.models import Usuario, Token
# Create your views here.

def index(request):
	context = {'participo':False}
	concurso = Concurso.objects.get(id=settings.CONCURSO)
	if request.user.is_authenticated() and concurso.estado:
		context['token'] = ""
		sw_token = False
		try:
			usuario = Usuario.objects.get(id=request.user.id)
			if 'token' in request.GET and 'user' in request.GET:
				participa = Participa(usuario=usuario,concurso=concurso)
				participa.save()
				return HttpResponseRedirect('/')
		except:
			pass
		query = Participa.objects.filter(usuario__id=request.user.id,concurso=concurso)
		if sw_token:
			if query:
				context['participo'] = True
			if usuario.has_token():
				context['token'] = usuario.get_token()
	return render_to_response('index.html',context, context_instance=RequestContext(request))