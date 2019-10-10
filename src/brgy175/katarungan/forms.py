from django import forms
<<<<<<< HEAD
from .models import Katarungan
=======
from .models import CaseRecord

CASE_STATUS_CHOICES = [
    ('CFA', 'CFA'),
    ('Withdraw', 'Withdraw'),
    ('Settled', 'Settled')
]
>>>>>>> 78286c588bff0a00c4598a0b18bcc318b72091d8


class CaseForm(forms.ModelForm):
    class Meta:
<<<<<<< HEAD
        Meta: Katarungan
        fields = ["case_no", "case_type", "complainant", "case_status",]
=======
        model = CaseRecord
        fields = { "resident_case", "case_no", "case_type", "complainant", "case_status"  }
    #FIXME how to add these into fields coming form residents
    # "first_name", "middle_name", "last_name", "address" 
>>>>>>> 78286c588bff0a00c4598a0b18bcc318b72091d8
