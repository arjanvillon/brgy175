from django.contrib import admin
from .models import IDForm, IndigencyForm, ClearanceForm, BusinessPermit, ScholarshipForm, BurialForm

# Register your models here.
admin.site.register(IDForm, IndigencyForm, ClearanceForm, BusinessPermit, ScholarshipForm, BurialForm)