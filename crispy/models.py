from django.db import models
from django.urls import reverse
# Create your models here.


class Patient(models.Model):
    """Patient Class """
    GENDER = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    last_name = models.CharField(max_length=50, blank=True)
    initials = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=50, blank=True)
    birthday = models.DateField(blank=True)
    gender = models.CharField(max_length=1, choices=GENDER, blank=True)
    # clinic_followup = models.CharField(max_length=100, blank=True)
    # past_history = models.CharField(max_length=100, blank=True)
    # allergy = models.CharField(max_length=50, blank=True)
    # management = models.CharField(max_length=100, blank=True)
    # date_registered = models.DateTimeField(auto_now_add=True)
    # nid = models.CharField(max_length=12, blank=True)

    class Meta:
        verbose_name = "patient"
        verbose_name_plural = "patients"

    @property
    def full_name(self):
        "Returns the person's full name."
        return '%s %s' % (self.initials, self.last_name)

    def __str__(self):
        return '%s %s' % (self.initials, self.last_name)

    def get_absolute_url(self):
        return reverse("patient_detail", kwargs={"pk": self.pk})


class History(models.Model):
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name='historys')
    time = models.DateTimeField(auto_now=True)
    symptoms = models.TextField(blank=True)
    diagnosis = models.CharField(max_length=50, blank=True)
    investigations = models.CharField(max_length=100, blank=True)
    bp = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return (self.patient.full_name)


class Drug(models.Model):
    drug_name = models.CharField(unique=True, max_length=50)
    unit_price = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True)
    date_of_expiry = models.DateField(blank=True)
    stock_Available = models.IntegerField(blank=True)

    def __str__(self):
        return str(self.drug_name)


class Dose(models.Model):
    dose = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return str(self.dose)


class Regim(models.Model):
    regim = models.CharField(max_length=12)

    def __str__(self):
        return str(self.regim)


class Prescription(models.Model):
    history = models.ForeignKey(History, on_delete=models.CASCADE)
    drug = models.ForeignKey(
        Drug, on_delete=models.SET_NULL, blank=True, null=True)
    dose = models.ForeignKey(
        Dose, on_delete=models.SET_NULL, blank=True, null=True)
    regim = models.ForeignKey(
        Regim, on_delete=models.SET_NULL, blank=True, null=True)
    no_of_tabs = models.IntegerField()
    pharmacy = models.BooleanField(null=True)

    def __str__(self):
        return str(self.history)
