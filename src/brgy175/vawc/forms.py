from django import forms
from .models import vawc

CASE_STATUS_CHOICES = [
    ('CFA', 'CFA'),
    ('Withdraw', 'Withdraw'),
    ('Settled', 'Settled')
]


class CaseForm(forms.ModelForm):
    case_status = forms.ChoiceField(choices=(CASE_STATUS_CHOICES))
    class Meta:
        Meta: vawc
        fields = "__all__"
 