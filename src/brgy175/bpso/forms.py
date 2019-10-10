from django import forms
from .models import bpso

class CaseForm(forms.ModelForm):

    class Meta:
        Meta: bpso
        fields = "__all__"
 