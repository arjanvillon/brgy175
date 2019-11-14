from django import forms
from announcement.models import Announcement

class AnnouncementForm(forms.ModelForm):
    class Meta():
        model = Announcement
        fields = ('author', 'title', 'text', 'picture')