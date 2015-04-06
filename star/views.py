from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings
from star.models import Concurso, Participa
# Create your views here.


def participantes(request):
	context = {}
	concurso = Concurso.objects.get(id=settings.CONCURSO)
	if concurso:
		context['lista'] = concurso.get_participantes()
	return render_to_response('lista.html',context, context_instance=RequestContext(request))