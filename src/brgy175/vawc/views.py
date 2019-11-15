from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import (View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.urls import reverse_lazy
from vawc import models
from django.contrib.auth.mixins import LoginRequiredMixin
from user_account.decorators import superadmin_vawc_only


class VawcListView(superadmin_vawc_only,LoginRequiredMixin,ListView):
    context_object_name = 'vawcs'
    model =  models.vawc
    template_name = 'vawc/vawcHome.html'
 
   
class VawcDetailView(superadmin_vawc_only,LoginRequiredMixin,DetailView):
    context_object_name = 'vawc_detail'
    model = models.vawc
    template_name = 'vawc/vawc_detail.html'

class VawcCreateView(superadmin_vawc_only,LoginRequiredMixin,CreateView):
    fields = ('case_no', 'case_type', 'convict', 'complainant', 'case_status')
    model = models.vawc


class VawcUpdateView(superadmin_vawc_only,LoginRequiredMixin,UpdateView):
    fields = ('case_type', 'case_status')
    model = models.vawc


class VawcDeleteView(superadmin_vawc_only,LoginRequiredMixin,DeleteView):
    model = models.vawc
    success_url = reverse_lazy('vawc:list')

