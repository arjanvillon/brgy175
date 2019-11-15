from django.shortcuts import render
from sk.models import Sk
from sk.forms import SkForm
from django.views.generic import (
    View, TemplateView,
    ListView, DetailView,
    CreateView, UpdateView,
    DeleteView
)

class SkHomeView(TemplateView):
    template_name = 'sk/skHome.html'
    
class SkCreateView(CreateView):
    form_class = SkForm
    model = Sk

class SkListView(ListView):
    context_object_name = 'sk_list'
    model = Sk

class SkDetailView(DetailView):
    context_object_name = 'sk_detail'
    model = Sk
    template_name = 'sk/sk_detail.html'

class SkUpdateView(UpdateView):
    form_class = SkForm
    model = Sk