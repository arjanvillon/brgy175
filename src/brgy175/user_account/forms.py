from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


SECTORS_CHOICES= [
    ('superadmin', 'Super Admin'),
    ('katarungan', 'Katarungang Pambarangay'),
    ('vawc', 'VAWC / BCPC'),
    ('badac', 'BADAC'),
    ('bpso', 'BPSO'),
    ('senior', 'PWD & Senior Dept'),
    ('sk', 'Sangguniang Kabataan'),
    ('assistance', 'Financial Assistance'),
]

class UserRegisterForm(UserCreationForm):
    full_name = forms.CharField(max_length=255,min_length=3)
    middle_initial = forms.CharField(max_length=3)
    last_name= forms.CharField(max_length=100)
    select_sectors= forms.CharField(label='Select Sector', widget=forms.Select(choices=SECTORS_CHOICES))
    
    
    

    class Meta:
        model = User
        fields = ['full_name', 'middle_initial' , 'last_name', 'select_sectors','password1', 'password2']
        
       