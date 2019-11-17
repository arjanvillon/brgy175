from django.db import models
from django.urls import reverse
from django.utils import timezone
from residents.models import Resident
from katarungan.choices import CASE_TYPE_CHOICES

class Katarungan(models.Model):
    case_no = models.CharField(max_length=14)
    case_type = models.CharField(max_length=30, choices=CASE_TYPE_CHOICES)
    complainant = models.CharField(max_length=30)
    case_status = models.CharField(max_length=8, default='CFA')
    convict = models.ForeignKey(Resident,related_name='convicted', on_delete=models.CASCADE, null=True)
    
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.case_no

    def get_absolute_url(self):
        return reverse("katarungan:detail", kwargs={"pk": self.pk})
        
    def cfa(self):
        self.case_status = "CFA"
        self.save()


    def settle(self):
        self.case_status = "Settled"
        self.save()

    def withdraw(self):
        self.case_status = "Withdraw"
        self.save()