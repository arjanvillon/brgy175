from django import forms
from .models import Resident
from crispy_forms.helper import FormHelper

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


class ResidentForm(forms.ModelForm):

    gender = forms.ChoiceField(choices=(GENDER_CHOICES))
    civil_status = forms.ChoiceField(choices=(CIVIL_STATUS_CHOICES))
    class Meta:
        model = Resident
        fields = "__all__"

        widgets = {
            'first_name':forms.TextInput(attrs={'placeholder':'First Name'}),
            'middle_name':forms.TextInput(attrs={'placeholder':'Middle Name'}),
            'last_name':forms.TextInput(attrs={'placeholder':'Last Name'}),
            'suffix':forms.TextInput(attrs={'placeholder':'Sr.', 'required':'False'}),
            'address':forms.TextInput(attrs={'placeholder':'Unit #, House #, Building, Street Name, Zone #'}),
            'date_of_birth':forms.TextInput(attrs={'placeholder':'MM / DD / YYYY'}),
            'place_of_birth':forms.TextInput(attrs={'placeholder':'City'}),
            'weight':forms.TextInput(attrs={'placeholder':'Kilogram'}),
            'height':forms.TextInput(attrs={'placeholder':'Centimeter'}),
            'contact_number':forms.TextInput(attrs={'placeholder':'09xx-xxx-xxxx'}),
            'nationality':forms.TextInput(attrs={'placeholder':'Filipino'}),
            'email_address':forms.TextInput(attrs={'placeholder':'e.g. juan@gmail.com'}),
            'Religion':forms.TextInput(attrs={'placeholder':'Catholic'}),
        }
        required = {
            'suffix': False,
        }
        # fields = ( "first_name", "middle_name", "last_name", "suffix", "address", "date_of_birth", "place_of_birth", "age", "weight", "height", "gender", "civil_status", "contact_number", "nationality", "email_address", "religion")
        # fields = { "first_name", "middle_name", "last_name", "suffix", "age", "address", "date_of_birth", "place_of_birth", "weight", "height", "gender", "civil_status", "contact_number", "nationality", "email_address", "religion", "citizen_id", "pwd_no", "is_senior", "is_fresh_grad", "is_pwd"}

    
    def __init__(self, *args, **kwargs):
        super(ResidentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.fields['suffix'].required = False
        self.fields['gender'].required = True
        self.fields['civil_status'].required = True
        