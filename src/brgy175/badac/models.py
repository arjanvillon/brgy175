from django.db import models
from django.urls import reverse
from django.utils import timezone
from residents.models import Resident


class FormBADAC(models.Model):
    case_no_badac = models.CharField(max_length=25)
    case_type_badac = models.CharField(max_length=30)
    complainant_badac = models.CharField(max_length=30)
    case_status_badac = models.CharField(max_length=8, default='Red')
    convict = models.ForeignKey(Resident, on_delete=models.CASCADE, null=True)

    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.case_no_badac

    def get_absolute_url(self):
        return reverse("badac:detail", kwargs={"pk": self.pk})


    def R(self):
        self.case_status_badac = "Red"
        self.save()

    def G(self):
        self.case_status_badac = "Green"
        self.save()

    def B(self):
        self.case_status_badac = "Blue"
        self.save()

    def Y(self):
        self.case_status_badac = "Yellow"
        self.save()
