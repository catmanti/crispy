# from crispy.crispy.models import Dose, Drug, Prescription, Regim
from django.contrib import admin
from crispy.models import Patient, History, Drug, Dose, Regim, Prescription
# Register your models here.
admin.site.register(Patient)
admin.site.register(History)
admin.site.register(Drug)
admin.site.register(Dose)
admin.site.register(Regim)
admin.site.register(Prescription)

