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
    url(r'^$', index),
)
