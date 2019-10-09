from django.contrib import admin
from .models import IDForm, IndigencyForm, ClearanceForm, BusinessPermit, ScholarshipForm, BurialForm

landingModels = [IDForm, IndigencyForm, ClearanceForm, BusinessPermit, ScholarshipForm, BurialForm]
admin.site.register(landingModels)