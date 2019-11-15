from django import forms
from sk.models import Project
from crispy_forms.helper import FormHelper

class ProjectForm(forms.ModelForm):
    class Meta():
        model = Project
        fields = ('project_name', 'project_details', 'officer', 'project_picture', 'start_date', 'end_date')

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False