from django.shortcuts import render
from residents.models import Resident
from . import models
from django.views.generic import (
    View, TemplateView,
    ListView, DetailView,
    CreateView, UpdateView,
    DeleteView
)

class SeniorIndexView(TemplateView):
    template_name = 'senior/senior_home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["senior"] = Resident.objects.filter(is_senior="Senior").all()
        return context
    

class SeniorListView(ListView):
    context_object_name = 'senior_list'
    model = Resident

class SeniorDetailView(DetailView):
    context_object_name = 'senior_detail'
    model = models.Senior
    template_name = 'senior/senior_detail.html'
