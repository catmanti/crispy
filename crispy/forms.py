from django import forms
from django.forms import HiddenInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Field
from crispy.models import Patient, History, Prescription

STATES = (
    ('', 'Choose...'),
    ('MG', 'Minas Gerais'),
    ('SP', 'Sao Paulo'),
    ('RJ', 'Rio de Janeiro')
)


class AddressForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput())
    address_1 = forms.CharField(
        label='Address',
        widget=forms.TextInput(attrs={'placeholder': '1234 Main St'})
    )
    address_2 = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Apartment, studio, or floor'})
    )
    city = forms.CharField()
    state = forms.ChoiceField(choices=STATES)
    zip_code = forms.CharField(label='Zip')
    check_me_out = forms.BooleanField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('email', css_class='form-group col-md-6 mb-0'),
                Column('password', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'address_1',
            'address_2',
            Row(
                Column('city', css_class='form-group col-md-6 mb-0'),
                Column('state', css_class='form-group col-md-4 mb-0'),
                Column('zip_code', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            'check_me_out',
            Submit('submit', 'Sign in')
        )


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'


class HistoryForm(forms.ModelForm):
    class Meta:
        model = History
        fields = ('patient', 'symptoms', 'diagnosis', 'investigations', 'bp')

    def __init__(self, *args, **kwargs):
        super(HistoryForm, self).__init__(*args, **kwargs)
        self.fields['patient'].widget = HiddenInput()


class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PrescriptionForm, self).__init__(*args, **kwargs)
        self.fields['history'].widget = HiddenInput()
