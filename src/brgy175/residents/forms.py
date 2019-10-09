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
        fields = { "first_name", "middle_name", "last_name", "suffix"}
        # fields = { "first_name", "middle_name", "last_name", "suffix", "age", "address", "date_of_birth", "place_of_birth", "weight", "height", "gender", "civil_status", "contact_number", "nationality", "email_address", "religion", "citizen_id", "pwd_no", "is_senior", "is_fresh_grad", "is_pwd"}