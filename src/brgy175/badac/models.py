from django.db import models
from residents.models import Resident

class badac(models.Model):
    resident_case = models.ForeignKey('residents.Resident', on_delete=models.CASCADE, null=True)
    case_no = models.CharField(max_length=14)
    case_type = models.CharField(max_length=30)
    complainant = models.CharField(max_length=50)
    case_status = models.CharField(max_length=8)