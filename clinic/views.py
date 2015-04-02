from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import ListView
from clinic.clinic_forms import AddPatientForm, AddPatientAddressForm
from clinic.models import Patient


class PatienList(ListView):
    template_name = 'clinic/patient_list.html'

    def get_queryset(self, **kwargs):
        patients = Patient.objects.all()
        return patients

    def get_context_data(self, **kwargs):
        context = super(PatienList, self).get_context_data(**kwargs)
        return context


@login_required(login_url='login')
def add_new_patient(request):
    context = dict()
    if request.method == 'POST':
        patient_form = AddPatientForm(request.POST or None)
        address_form = AddPatientAddressForm(request.POST or None)
        if patient_form.is_valid() and address_form.is_valid():
            patient = patient_form.save(commit=False)
            patient.save()
            address = address_form.save(commit=False)
            address.patient = patient
            address.save()
            return HttpResponseRedirect(reverse('patient_list'))
        else:
            print 'INVALID', patient_form.errors, address_form.errors
    context['patient_form'] = AddPatientForm(None)
    context['address_form'] = AddPatientAddressForm(None)
    request_context = RequestContext(request, context)
    return render_to_response('clinic/add_new_patient.html',
                              request_context)