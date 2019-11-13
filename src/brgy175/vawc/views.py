from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import (View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.urls import reverse_lazy
# from katarungan.forms import CaseForm
from vawc import models

class VawcListView(ListView):
    context_object_name = 'vawcs'
    model =  models.vawc

class VawcDetailView(DetailView):
    context_object_name = 'vawc_detail'
    model = models.vawc
    template_name = 'vawc/vawc_detail.html'

class VawcCreateView(CreateView):
    fields = ('case_no', 'case_type', 'convict', 'complainant', 'case_status')
    model = models.vawc

class VawcUpdateView(UpdateView):
    fields = ('case_type', 'case_status')
    model = models.vawc

class VawcDeleteView(DeleteView):
    model = models.vawc
    success_url = reverse_lazy('vawc:list')
