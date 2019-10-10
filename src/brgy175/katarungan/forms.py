from django import forms
from .models import Katarungan

class CaseForm(forms.ModelForm):
    class Meta:
        Meta: Katarungan
        fields = ["case_no", "case_type", "complainant", "case_status",]