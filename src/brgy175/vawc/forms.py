from django import forms
from .models import vawc

class CaseForm(forms.ModelForm):

    class Meta:
        Meta: vawc
        fields = "__all__"
 