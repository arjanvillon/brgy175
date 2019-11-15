from django.db import models
from django.utils import timezone
from residents.models import Resident
from django.urls import reverse

# Create your models here.
class Sk(models.Model):
    project_name = models.CharField(max_length=80)
    project_details = models.TextField()
    officer = models.ForeignKey(Resident, on_delete=models.CASCADE)
    project_picture = models.ImageField(upload_to='sk_project_pics', default='default.jpg')
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now)

     
    def __str__(self):
        return self.project_name
        
    def get_absolute_url(self):
        return reverse("sk:sk_detail", kwargs={"pk": self.pk})