# -*- coding: utf-8 -*-
import datetime
from django.forms import ModelForm, CharField, DateField, DateInput
from clinic.models import Patient, PatientAddress

__author__ = 'jesuscc29'


class AddPatientForm(ModelForm):
    birthday = DateField(widget=DateInput(format='%Y-%m-%d'),
                         input_formats=('%Y-%m-%d',),
                         initial=datetime.date.today(),
                         label='Fecha de Nacimiento',
                         required=True)

    class Meta:
        model = Patient


class AddPatientAddressForm(ModelForm):
    class Meta:
        model = PatientAddress
        exclude = ['patient']