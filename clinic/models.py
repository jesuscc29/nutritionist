import datetime
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Patient(models.Model):
    GENDER_CHOICES = (
        (0, 'Hombre'),
        (1, 'Mujer')
    )
    name = models.CharField(max_length=150, verbose_name='Nombre(s)')
    last_name = models.CharField(max_length=150, verbose_name='Apellido(s)')
    birthday = models.DateField(default=datetime.date.today(),
                                verbose_name='Fecha de Nacimiento')
    gender = models.SmallIntegerField(verbose_name='Sexo', default=0,
                                      choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=64, verbose_name='Telefono',
                                    blank=True, null=True)
    email = models.CharField(max_length=128, verbose_name='Correo Electronico',
                             blank=True, null=True)
    notes = models.TextField(verbose_name='Notas', blank=True, null=True)

    def __str__(self):
        return self.name + ' ' + self.last_name

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'


@python_2_unicode_compatible
class PatientAddress(models.Model):
    street_number = models.CharField(max_length=150, verbose_name='Calle y Numero')
    neighborhood = models.CharField(max_length=150, verbose_name='Colonia')
    zipcode = models.CharField(max_length=16, verbose_name='Codigo Postal',
                               blank=True, null=True)
    municipality = models.CharField(max_length=150, verbose_name='Municipio')
    state = models.CharField(max_length=150, verbose_name='Estado')
    patient = models.ForeignKey(Patient, verbose_name='Paciente')

    def __str__(self):
        return ' '.join([
            self.street_number, self.neighborhood, self.municipality,
            self.state, ' - ', self.patient.name, self.patient.last_name
        ])

    class Meta:
        verbose_name = 'Direccion'
        verbose_name_plural = 'Direcciones'