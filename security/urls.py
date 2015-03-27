from django.conf.urls import patterns, include, url
from security import views

urlpatterns = patterns('',
	url('^$', views.index),
	url('^(?P<codigo>\d{1,})/$', views.index),
	url('^editar/(?P<codigo>\d{1,})/$', views.index),
	url('^password/(?P<codigo>\d{1,})/$', views.usuariox_pass),
	url('^bk/is_administrador.json$', views.is_administrador)
)
