from django import forms

from .models import FormBPSO


class FormBPSOForm(forms.ModelForm):
    class Meta():
        model = FormBPSO
        fields = ('case_no_bpso','case_type_bpso', 'convict', 'complainant_bpso')
