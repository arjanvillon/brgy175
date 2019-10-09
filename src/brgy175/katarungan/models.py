from django.db import models

class CaseRecord(models.Model):
    case_no = models.CharField(max_length=14)
    case_type = models.CharField(max_length=30)
    complainant = models.CharField(max_length=50)
    case_status = models.CharField(max_length=8)