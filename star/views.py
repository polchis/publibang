from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings
from star.models import Concurso, Participa, TokenParticipa, Lugar
from django.contrib.auth.decorators import login_required
from security.models import Usuario
import requests
import uuid
# Create your views here.


def participantes(request):
	context = {}
	concurso = Concurso.objects.get(id=settings.CONCURSO)
	if concurso:
		context['lista'] = concurso.get_participantes()
	return render_to_response('lista.html',context, context_instance=RequestContext(request))

@login_required
def participa_enviar(request,lugar):
	context = {}
	concurso = Concurso.objects.get(id=settings.CONCURSO)
	if concurso.estado:
		query = Participa.objects.filter(usuario__id=request.user.id, concurso=concurso)
		if query:
			return HttpResponseRedirect("/")
		else:
			q_token = TokenParticipa.objects.filter(usuario__id = request.user.id)
			if q_token:
				r = requests.get(settings.URL_RECIVE+q_token[0].frase)
				if r.status_code == 200:
					return HttpResponseRedirect(r.text)
				else:
					return HttpResponseRedirect('/')
			try:
				usuario = Usuario.objects.get(id=request.user.id)
				while 1:
					frase = uuid.uuid4()
					lugar = Lugar.objects.get(id=lugar)
					query_token = TokenParticipa.objects.filter(frase=frase)
					if not query_token:
						break
				token = TokenParticipa(usuario=usuario, frase=str(frase), lugar=lugar)
				token.save()
				r = requests.get(settings.URL_RECIVE+str(token.frase))
				if r.status_code == 200:
					return HttpResponseRedirect(r.text)
				else:
					return HttpResponseRedirect('/')
			except:
				pass
	return HttpResponseRedirect('/')

@login_required
def participa_recibir(request):
	frase=request.GET.get('token')
	if frase:
		q = TokenParticipa.objects.filter(frase=frase)
		if q:
			usuario = Usuario.objects.get(id=request.user.id)
			concurso = Concurso.objects.get(id=settings.CONCURSO)
			token = q[0]
			participa = Participa(usuario=usuario, concurso=concurso, lugar=token.lugar)
			participa.save()
			token.delete()
			return HttpResponseRedirect('/')
	return HttpResponseRedirect('/')
