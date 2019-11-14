from django.db import models
from django.utils import timezone
from django.urls import reverse
from residents.models import Resident

# Create your models here.

class Scholar(models.Model):
    student = models.OneToOneField('residents.Resident', related_name='students', on_delete=models.CASCADE)
    school = models.CharField(max_length=50)
    year_level = models.CharField(max_length=10)
    course = models.CharField(max_length=100)
    # Father Info
    father_name = models.CharField(max_length=50)
    father_address = models.TextField()
    father_age = models.PositiveIntegerField()
    father_occupation = models.CharField(max_length=30)
    father_mobile = models.CharField(max_length=11)
    father_precint = models.CharField(max_length=30)
    father_salary = models.PositiveIntegerField()
    # Mother Info
    mother_name = models.CharField(max_length=50)
    mother_address = models.TextField()
    mother_age = models.PositiveIntegerField()
    mother_occupation = models.CharField(max_length=30)
    mother_mobile = models.CharField(max_length=11)
    mother_precint = models.CharField(max_length=30)
    mother_salary = models.PositiveIntegerField()

    is_approved = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)

    def approve(self):
        self.is_approved = True
        self.save()

    def get_absolute_url(self):
        return reverse('assistance:scholar_detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.school
    

class Burial(models.Model):
    corpse = models.ForeignKey('residents.Resident', on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    date_of_death = models.DateField()
    interment_address = models.TextField()
    interment_date = models.DateField()

    # Claimant / Requestor Info
    name = models.CharField(max_length=50)
    address = models.TextField()
    relationship = models.CharField(max_length=20)

    is_approved = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)

    def approve(self):
        self.is_approved = True
        self.save()

    def get_absolute_url(self):
        return reverse('assistance:burial_detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.name
    
    