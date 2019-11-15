from django.db import models
from django.urls import reverse
from django.utils import timezone
from residents.models import Resident


class FormBADAC(models.Model):
    case_no_badac = models.CharField(max_length=25)
    case_type_badac = models.CharField(max_length=30)
    complainant_badac = models.CharField(max_length=30)
    case_status_badac = models.CharField(max_length=8, default='CFA')
    convict = models.ForeignKey(Resident, on_delete=models.CASCADE, null=True)

    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.case_no_badac

    def get_absolute_url(self):
        return reverse("badac:detail", kwargs={"pk": self.pk})

    def settle(self):
        self.case_status_badac = "Settled"
        self.save()

    def withdraw(self):
        self.case_status_badac = "Withdraw"
        self.save()

