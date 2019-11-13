from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.urls import reverse_lazy
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from assistance.models import Scholar, Burial
from assistance.forms import ScholarForm, BurialForm

class Assistance(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    template_name = 'assistance/assistance_home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Scholar Queries
        context['scholar_all'] = Scholar.objects.all().count()
        context['scholar_approved'] = Scholar.objects.filter(is_approved=True).count()
        context['scholar_pending'] = Scholar.objects.filter(is_approved=False).count()
        # Burial Queries
        context['burial_all'] = Burial.objects.all().count()
        context['burial_approved'] = Burial.objects.filter(is_approved=True).count()
        context['burial_pending'] = Burial.objects.filter(is_approved=False).count()
        return context

class ScholarListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = Scholar

    def get_queryset(self):
        return Scholar.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')

class ScholarDetailView(LoginRequiredMixin, DetailView):
    login_url = '/login/'
    model = Scholar

class ScholarCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    form_class = ScholarForm
    model = Scholar

class ScholarDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    model = Scholar
    success_url = reverse_lazy('scholar_list')

@login_required
def approve_scholar(request,pk):
    scholar = get_object_or_404(Scholar, pk=pk)
    scholar.approve()
    return redirect('assistance:scholar_detail', pk=pk)

class BurialListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = Burial

    def get_queryset(self):
        return Burial.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')

class BurialDetailView(LoginRequiredMixin, DetailView):
    login_url = '/login/'
    model = Burial

class BurialCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    form_class = BurialForm
    model = Burial
class BurialDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    model = Burial
    success_url = reverse_lazy('burial_list')

@login_required
def approve_burial(request,pk):
    burial = get_object_or_404(Burial, pk=pk)
    burial.approve()
    return redirect('assistance:burial_detail', pk=pk)

    
