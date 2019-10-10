from django import forms
from .models import CaseRecord

CASE_STATUS_CHOICES = [
    ('CFA', 'CFA'),
    ('Withdraw', 'Withdraw'),
    ('Settled', 'Settled')
]


class CaseForm(forms.ModelForm):
    case_status = forms.ChoiceField(choices=(CASE_STATUS_CHOICES))
    class Meta:
        model = CaseRecord
        fields = { "resident_case", "case_no", "case_type", "complainant", "case_status"  }
    #FIXME how to add these into fields coming form residents
    # "first_name", "middle_name", "last_name", "address" 