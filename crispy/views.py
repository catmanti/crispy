from django.shortcuts import render,  get_object_or_404
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse_lazy

from crispy.forms import HistoryForm
from crispy.models import Patient, History, Prescription


class PatientListView(generic.ListView):
    model = Patient


class PatientDetailView(generic.DetailView):
    model = Patient

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(PatientDetailView, self).get_context_data(**kwargs)
        history = History.objects.filter(patient=self.kwargs['pk'])
        # Create any data and add it to the context
        context['history'] = history
        return context


class PatientCreateView(generic.CreateView):
    model = Patient
    fields = '__all__'


class PatientUpdateView(generic.UpdateView):
    model = Patient
    fields = '__all__'


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
    ptid = None
    success_url = reverse_lazy('patients')
    extra_context = {'myurl': 'patients'}

    def get_initial(self):
        patient = get_object_or_404(Patient, pk=self.kwargs.get('ptid'))
        return {
            'patient': patient
        }

    def get_context_data(self, **kwargs):
        context = super(HistoryCreateView, self).get_context_data(**kwargs)
        ptid = get_object_or_404(Patient, pk=self.kwargs.get('ptid'))
        context['myid'] = ptid.id
        context['myurl'] = 'patient_detail'
        return context


class HistoryUpdateView(generic.UpdateView):
    model = History
    fields = '__all__'
    extra_context = {
        'myurl': 'history_detail',
        'myid': 'history.id'
    }


class HistoryDeleteView(generic.DeleteView):
    model = History
    success_url = reverse_lazy('patients')


def test(request):
    return render(request, 'crispy/test.html', {'columns': ['man', 'chan', 'can', 'van']})
