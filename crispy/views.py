from django.shortcuts import render,  get_object_or_404
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse_lazy

from crispy.forms import HistoryForm, PrescriptionForm
from crispy.models import Patient, History, Prescription


class PatientListView(generic.ListView):
    model = Patient


class PatientDetailView(generic.DetailView):
    model = Patient

    def get_context_data(self, **kwargs):
        context = super(PatientDetailView, self).get_context_data(**kwargs)
        history = History.objects.filter(patient=self.kwargs['pk'])
        context['history'] = history
        return context


class PatientCreateView(generic.CreateView):
    model = Patient
    fields = '__all__'


class PatientUpdateView(generic.UpdateView):
    model = Patient
    fields = '__all__'
    extra_context = {'isUpdate': True}


class PatientDeleteView(generic.DeleteView):
    model = Patient
    success_url = reverse_lazy('patients')


class HistoryDetailView(generic.DetailView):
    model = History
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(HistoryDetailView, self).get_context_data(**kwargs)
        prescription = Prescription.objects.filter(history=self.kwargs['pk'])
        context['prescription'] = prescription
        return context


class HistoryCreateView(generic.CreateView):
    model = History
    form_class = HistoryForm

    def get_initial(self):
        patient = get_object_or_404(Patient, pk=self.kwargs.get('ptid'))
        return {
            'patient': patient
        }

    def get_context_data(self, **kwargs):
        """ To function history_form.html back button add id and url """
        context = super(HistoryCreateView, self).get_context_data(**kwargs)
        ptid = get_object_or_404(Patient, pk=self.kwargs.get('ptid'))
        context['myid'] = ptid.id
        context['myurl'] = 'patient_detail'
        return context


class HistoryUpdateView(generic.UpdateView):
    model = History
    fields = '__all__'
    extra_context = {'isUpdate': True}


class HistoryDeleteView(generic.DeleteView):
    model = History
    success_url = reverse_lazy('patients')


class PrescriptionCreateView(generic.CreateView):
    model = Prescription
    # fields = '__all__'
    form_class = PrescriptionForm

    def get_initial(self):
        history = get_object_or_404(History, pk=self.kwargs.get('hisid'))
        return {
            'history': history
        }


class PrescriptionDetailView(generic.DetailView):
    model = Prescription
    fields = '__all__'


def test(request):
    return render(request, 'crispy/test.html', {'columns': ['man', 'chan', 'can', 'van']})
