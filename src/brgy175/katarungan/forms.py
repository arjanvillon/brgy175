from django import forms
from .models import Katarungan

CASE_STATUS_CHOICES = [
    ('CFA', 'CFA'),
    ('Withdraw', 'Withdraw'),
    ('Settled', 'Settled')
]

class CaseForm(forms.ModelForm):
    case_status = forms.ChoiceField(choices=(CASE_STATUS_CHOICES))

    class Meta:
        model = Katarungan
        fields = "__all__"