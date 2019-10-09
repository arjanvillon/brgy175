from django import forms
from .models import CaseRecord

CASE_STATUS_CHOICES = [
    ('CFA', 'cfa'),
    ('Withdraw', 'withdraw'),
    ('Settled', 'settled')
]

class CaseForm(forms.ModelForm):
    case_status = forms.ChoiceField(choices=(CASE_STATUS_CHOICES))
    class Meta:
        model = CaseRecord
        fields = { "case_no", "first_name", "middle_name", "last_name", "address", "case_type", "complainant", "case_status"  }