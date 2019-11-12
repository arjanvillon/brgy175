from django.db import models
from django.urls import reverse
from django.utils import timezone
from residents.models import Resident

class Katarungan(models.Model):
    case_no = models.CharField(max_length=14)
    case_type = models.CharField(max_length=30)
    complainant = models.CharField(max_length=30)
    case_status = models.CharField(max_length=8)
    convict = models.ForeignKey(Resident, on_delete=models.CASCADE, null=True)

    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.case_no

    def get_absolute_url(self):
        return reverse("katarungan:detail", kwargs={"pk": self.pk})