from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'publibang.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'security.views.login'),
    url(r'^logout/$', 'security.views.onlogout'),
    url(r'^$', 'inicio.views.index'),
    url(r'^registro/$', 'inicio.views.vista_registro'),
)
