from django.db import models
from django.urls import reverse
from residents.models import Resident

class vawc(models.Model):
    case_no = models.CharField(max_length=14)
    case_type = models.CharField(max_length=30)
    complainant = models.CharField(max_length=30)
    case_status = models.CharField(max_length=8)
    convict = models.ForeignKey(Resident, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.case_no

    def get_absolute_url(self):
        return reverse("vawc:detail", kwargs={"pk": self.pk})

    # def __unicode__(self):
    #     return "{0} {1} {2}".format(self.pk, self.case_no, self.case_type, self.complainant, self.case_status, self.c_resident)