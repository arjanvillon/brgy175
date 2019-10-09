from django import forms
from .models import IDForm, IndigencyForm, ClearanceForm, BusinessPermit, ScholarshipForm, BurialForm


class Form_id(forms.ModelForm):

    class Meta:
        Meta: IDForm
        fields= ['resident','con_person','con_person_address','con_person_relationship','con_person_mobile',]


class Form_idigent(forms.ModelForm):

    class Meta:
        Meta: IndigencyForm
        fields= ['ccwd','dswd_medical','in_birth_certificate','solo_parent','philhealth','burial_assistance','medical_assistance','financial_assistance','educational_assistance','dswd_financial']

class Form_clearance(forms.ModelForm):

    class Meta:
        Meta: ClearanceForm
        fields= ['bail_bon','bank','cl_birth_certificate','mayors_permit','meralco','personal_id','sss','excavation_permit','travel','loan,','indigency','building_permit','senior_citizan','local_employment','maynilad','barangay_id','tricycle_franchise','lipat_bahay','pnp','postal_id','business_license','motor_loan','bir','nha',]

class Form_business(forms.ModelForm):

    class Meta:
        Meta: BusinessPermit
        fields= ['barangay_permit','city_permit','business_address','business_name']

class Form_scholar(forms.ModelForm):

    class Meta:
        Meta: ScholarshipForm
        fields = ['father_name','father_address','father_age','father_occupation','father_mobile','father_precint','father_salary','mother_name','mother_address','mother_age','mother_occupation','mother_mobile','mother_precint','mother_salary',]

class Form_burial(forms.ModeForm):

    class Meta:
        Meta: BurialForm
        fields = ['burial_name','burial_address','burial_relation','burial_relation','burial_birth','burial_death','burial_interment_place','burial_interment_date']














