#encoding:utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import index

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'publibang.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'security.views.login'),
    url(r'^logout/$', 'security.views.onlogout'),
    url(r'^registro/$', 'security.views.registro'),
    url(r'^participa/enviar/(?P<lugar>\d{1,})$', 'star.views.participa_enviar'),
    url(r'^participa/recibir/$', 'star.views.participa_recibir'),
    # url(r'^ganador/$', 'security.views.ganador'),
    url(r'^participantes/$', 'star.views.participantes'),

    url(r'^$', index),
)
