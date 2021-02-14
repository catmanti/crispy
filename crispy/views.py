from django.shortcuts import render,  get_object_or_404
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse_lazy

from crispy.forms import AddressForm, PatientForm
from crispy.models import Patient, History


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


def test(request):
    return render(request, 'crispy/test.html', {'columns': ['man', 'chan', 'can', 'van']})
