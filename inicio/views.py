from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from inicio.models import Registro
from django.template import RequestContext
# Create your views here.

def index(request):
	obtener=Registro.objects.all()
	return render_to_response('index.html',{'obtener':obtener}, context_instance=RequestContext(request))
def vista_registro(request):
	obtener=Registro.objects.all()
	return render_to_response('registro.html',{'obtener':obtener}, context_instance=RequestContext(request))
def vista_lista(request):
	obtener=Registro.objects.all()
	return render_to_response('index.html',{'obtener':obtener}, context_instance=RequestContext(request))
def vista_ganador(request):
	obtener=Registro.objects.all()
	return render_to_response('index.html',{'obtener':obtener}, context_instance=RequestContext(request))

def vista_(request):
	obtener=Registro.objects.all()
	return render_to_response('index.html',{'obtener':obtener}, context_instance=RequestContext(request))
