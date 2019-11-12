from django import forms
from assistance.models import Scholar, Burial

class ScholarForm(forms.ModelForm):
    class Meta():
        model = Scholar
        fields = ('student', 'school', 'year_level', 'course', 'father_name', 'father_address', 'father_age', 'father_occupation', 'father_mobile', 'father_mobile', 'father_precint', 'father_salary', 'mother_name', 'mother_address', 'mother_age', 'mother_occupation', 'mother_mobile', 'mother_precint', 'mother_salary')

class BurialForm(forms.ModelForm):
    class Meta():
        model = Burial
        fields = ('corpse', 'date_of_birth', 'date_of_death', 'interment_address', 'interment_date', 'name', 'address', 'relationship')
