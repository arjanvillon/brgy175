from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.urls import reverse_lazy
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from announcement.models import Announcement
from announcement.forms import AnnouncementForm
# Create your views here.

class AnnouncementListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = Announcement
    
    def get_queryset(self):
        return Announcement.objects.all().order_by('-created_date')

class AnnouncementDetailView(LoginRequiredMixin, DetailView):
    login_url = '/login/'
    model = Announcement

class AnnouncementCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    form_class = AnnouncementForm
    model = Announcement

class AnnouncementUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    form_class = AnnouncementForm
    model = Announcement

class AnnouncementDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    model = Announcement
    success_url = reverse_lazy('announcement:announcement_list')
