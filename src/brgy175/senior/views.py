from django.shortcuts import render
from residents.models import Resident
from . import models
from django.views.generic import (
    View, TemplateView,
    ListView, DetailView,
    CreateView, UpdateView,
    DeleteView
)

class SeniorListView(ListView):
    context_object_name = 'senior_list'
    model = models.Senior

class SeniorDetailView(DetailView):
    context_object_name = 'senior_detail'
    model = models.Senior
    template_name = 'senior/senior_detail.html'
