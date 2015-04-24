#encoding:utf-8
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings
from star.models import Concurso, Participa, Lugar
from security.models import Usuario, Token
from datetime import datetime
from pytz import timezone
from django.utils.timezone import utc

# Create your views here.
def convert_timedelta_to_str(timed):
	total_secs = timed.seconds
	secs = total_secs % 60
	total_mins = total_secs / 60
	mins = total_mins % 60
	hours = total_mins / 60
	return (secs, mins, hours)

def index(request):
	context = {'participo':False}
	concurso = Concurso.objects.get(id=settings.CONCURSO)
	context['time_start'] = "00:00:00:00"
	if concurso:
		time_faltante = concurso.fin - datetime.utcnow().replace(tzinfo=utc)
		parse_to_str = convert_timedelta_to_str(time_faltante)
		context['time_start'] = "%02d:%02d:%02d:%02d"%(time_faltante.days, parse_to_str[2], parse_to_str[1], parse_to_str[0])
	if request.user.is_authenticated() and concurso.estado:
		context['lugares'] = Lugar.objects.filter(estado=True)
		query = Participa.objects.filter(usuario__id=request.user.id, concurso=concurso)
		if query:
			context['participo'] = True
	return render_to_response('index.html', context, context_instance=RequestContext(request))
