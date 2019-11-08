from django.db import models
from residents.models import Resident

class Senior(models.Model):
    senior_id = models.CharField(max_length=8)
    resident = models.ForeignKey(Resident,  on_delete=models.PROTECT)

    def __str__(self):
        return self.senior_id