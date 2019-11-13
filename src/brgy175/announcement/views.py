from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.urls import reverse_lazy
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from announcement.models import Announcement
from announcement.forms import AnnouncementForm
# Create your views here.

class AnnouncementListView(ListView):
    model = Announcement
    
    def get_queryset(self):
        return Announcement.objects.all().order_by('-created_date')

class AnnouncementDetailView(DetailView):
    model = Announcement

class AnnouncementCreateView(CreateView):
    form_class = AnnouncementForm
    model = Announcement

class AnnouncementUpdateView(UpdateView):
    form_class = AnnouncementForm
    model = Announcement

class AnnouncementDeleteView(DeleteView):
    model = Announcement
    success_url = reverse_lazy('announcement:announcement_list')
