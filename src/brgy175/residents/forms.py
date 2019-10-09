from django import forms
from .models import Resident

GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
]

CIVIL_STATUS_CHOICES = [
    ('Married', 'Married'),
    ('Single', 'Single'),
    ('Widow', 'Widow'),
    ('Widower', 'Widower'),
    ('Separated', 'Separated'),
]

class ResidentBasicForm(forms.ModelForm):
    class Meta:
        model = Resident
        fields = { "place_of_birth", "weight", "height", "gender", "civil_status", "contact_number", "nationality", "email_address", "religion", "citizen_id", "pwd_no", "is_senior", "is_fresh_grad", "is_pwd"}