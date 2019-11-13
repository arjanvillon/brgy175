from django.shortcuts import render
from django.views.generic import (
    View, TemplateView,
    ListView, DetailView,
    CreateView, UpdateView,
    DeleteView
)

class SkHomeView(TemplateView):
    template_name = 'sk/skHome.html'
    
