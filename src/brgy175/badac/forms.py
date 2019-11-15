from django import forms

from .models import FormBADAC


class FormBADACForm(forms.ModelForm):
    class Meta():
        model = FormBADAC
        fields = ('case_no_badac','case_type_badac', 'convict', 'complainant_badac')
