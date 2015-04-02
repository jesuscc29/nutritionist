# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from .views import *

__author__ = 'jesuscc29'

urlpatterns = patterns('',
                       url(r'^pacientes/$', PatienList.as_view(),
                           name='patient_list'),
                       url(r'^pacientes/nuevo_paciente/$', add_new_patient,
                           name='add_new_patient'),
)