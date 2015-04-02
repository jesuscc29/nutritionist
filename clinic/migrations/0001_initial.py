# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150, verbose_name=b'Nombre(s)')),
                ('last_name', models.CharField(max_length=150, verbose_name=b'Apellido(s)')),
                ('birthday', models.DateField(default=datetime.date(2015, 4, 2), verbose_name=b'Fecha de Nacimiento')),
                ('gender', models.SmallIntegerField(default=0, verbose_name=b'Sexo', choices=[(0, b'Hombre'), (1, b'Mujer')])),
                ('phone_numebr', models.CharField(max_length=64, null=True, verbose_name=b'Telefono', blank=True)),
                ('emai', models.CharField(max_length=128, null=True, verbose_name=b'Correo Electronico', blank=True)),
                ('notes', models.TextField(null=True, verbose_name=b'Notas', blank=True)),
            ],
            options={
                'verbose_name': 'Paciente',
                'verbose_name_plural': 'Pacientes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PatientAddress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('street_number', models.CharField(max_length=150, verbose_name=b'Calle y Numero')),
                ('neighborhood', models.CharField(max_length=150, verbose_name=b'Colonia')),
                ('zipcode', models.CharField(max_length=16, null=True, verbose_name=b'Codigo Postal', blank=True)),
                ('municipality', models.CharField(max_length=150, verbose_name=b'Municipio')),
                ('state', models.CharField(max_length=150, verbose_name=b'Estado')),
                ('patient', models.ForeignKey(verbose_name=b'Paciente', to='clinic.Patient')),
            ],
            options={
                'verbose_name': 'Direccion',
                'verbose_name_plural': 'Direcciones',
            },
            bases=(models.Model,),
        ),
    ]
