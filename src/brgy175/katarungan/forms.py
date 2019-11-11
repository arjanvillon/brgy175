from django import forms
from .models import Katarungan

class KatarunganForm(forms.ModelForm):
    class Meta():
        model = Katarungan
        fields = ('case_no', 'case_type', 'convict', 'complainant')