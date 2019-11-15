from django import forms
from django.contrib.auth.models import User
from .models import Account
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import TextInput


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
    # first_name = forms.CharField(max_length=255,min_length=3)
    # middle_name = forms.CharField(max_length=3)
    # last_name= forms.CharField(max_length=100)
    sector= forms.CharField(label='Select Sector', widget=forms.Select(choices=SECTORS_CHOICES))

    class Meta:
        model = Account
        fields = ("username","email","first_name","middle_name","last_name","sector","password1","password2")
        widgets = {
            'name': TextInput(attrs={'autocomplete': 'false'}),
        }
        # ,"middle_name","last_name","sector"
class LoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ['username','password']
