from django.shortcuts import render
from sk.models import Project
from sk.forms import ProjectForm
from django.views.generic import (
    View, TemplateView,
    ListView, DetailView,
    CreateView, UpdateView,
    DeleteView
)
from django.urls import reverse_lazy

class SkHomeView(TemplateView):
    template_name = 'sk/skHome.html'
    
class ProjectCreateView(CreateView):
    form_class = ProjectForm
    model = Project

class ProjectListView(ListView):
    context_object_name = 'project_list'
    model = Project

class ProjectDetailView(DetailView):
    context_object_name = 'project_detail'
    model = Project
    template_name = 'sk/project_detail.html'

class ProjectUpdateView(UpdateView):
    form_class = ProjectForm
    model = Project

class ProjectDeleteView(DeleteView):
    model = Project
    success_url = reverse_lazy('sk:project_list')