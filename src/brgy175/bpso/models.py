from django.db import models
from django.urls import reverse
from django.utils import timezone
from residents.models import Resident


class FormBPSO(models.Model):
    case_no_bpso = models.CharField(max_length=14)
    case_type_bpso = models.CharField(max_length=30)
    complainant_bpso = models.CharField(max_length=30)
    case_status_bpso = models.CharField(max_length=8, default='CFA')
    convict = models.ForeignKey(Resident, on_delete=models.CASCADE, null=True)

    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.case_no_bpso

    def get_absolute_url(self):
        return reverse("bpso:detail", kwargs={"pk": self.pk})

    def settle(self):
        self.case_status_bpso = "Settled"
        self.save()

    def withdraw(self):
        self.case_status_bpso = "Withdraw"
        self.save()

