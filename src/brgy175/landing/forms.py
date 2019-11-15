from django import forms
from .models import (  IDForm, IndigencyForm, ClearanceForm,
                     BusinessPermit, ScholarshipForm, BurialForm)
from residents.models import Resident

class FormId(forms.ModelForm):

    class Meta:
        model = IDForm
        # exclude = ('resident_idform',)
        fields = "__all__"


class FormIdigent(forms.ModelForm):

    class Meta:
        model = IndigencyForm
        exclude = ('resident_indigency',)

class FormClearance(forms.ModelForm):

    class Meta:
        model = ClearanceForm
        exclude = ('resident_clearance',)


class FormBusiness(forms.ModelForm):

    class Meta:
        model = BusinessPermit
        exclude = ('resident_business',)

class FormScholar(forms.ModelForm):

    class Meta:
        model = ScholarshipForm
        exclude = ('resident_scholarship',)

class FormBurial(forms.ModelForm):

    class Meta:
        model = BurialForm
        exclude = ('resident_burial',)










