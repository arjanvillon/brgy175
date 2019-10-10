from django import forms
from .models import IDForm, IndigencyForm, ClearanceForm, BusinessPermit, ScholarshipForm, BurialForm


class Form_id(forms.ModelForm):

    class Meta:
        model= IDForm
        fields= "__all__"


class Form_idigent(forms.ModelForm):

    class Meta:
        model= IndigencyForm
        fields= "__all__"

class Form_clearance(forms.ModelForm):

    class Meta:
        model= ClearanceForm
        fields= "__all__"


class Form_business(forms.ModelForm):

    class Meta:
        model= BusinessPermit
        fields= "__all__"

class Form_scholar(forms.ModelForm):

    class Meta:
        model= ScholarshipForm
        fields= "__all__"

class Form_burial(forms.ModelForm):

    class Meta:
        model= BurialForm
        fields= "__all__"










