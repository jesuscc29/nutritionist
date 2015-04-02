from django.conf.urls import patterns, include, url
from django.contrib import admin
from nutrition import settings
from .views import *

urlpatterns = patterns('',
    # Examples:
    url(r'^login/$', user_login, name='login'),
    url(r'^logout$', logout_page, name='logout'),
    url(r'^home/$', home, name='home'),
    url(r'^clinica/', include('clinic.urls')),

    url(r'^admin/', include(admin.site.urls)),

    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
     {'document_root': settings.STATIC_ROOT}),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
     {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
)
