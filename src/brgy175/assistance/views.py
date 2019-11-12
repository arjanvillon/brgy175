from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.urls import reverse_lazy
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from assistance.models import Scholar, Burial
from assistance.forms import ScholarForm, BurialForm

class Assistance(TemplateView):
    template_name = 'assistance/assistance_home.html'
    model = Scholar

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['scholar_count'] = Scholar.objects.all().count()
        context['scholar_approved'] = Scholar.objects.filter(is_approved=True).count()
        return context

class ScholarListView(ListView):
    model = Scholar

    def get_queryset(self):
        return Scholar.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')

class ScholarDetailView(DetailView):
    model = Scholar

class ScholarCreateView(CreateView):
    form_class = ScholarForm
    model = Scholar

class ScholarDeleteView(DeleteView):
    model = Scholar
    success_url = reverse_lazy('scholar_list')

@login_required
def approve_scholar(request,pk):
    scholar = get_object_or_404(Scholar, pk=pk)
    scholar.approve()
    return redirect('assistance:scholar_detail', pk=pk)

class BurialListView(ListView):
    model = Burial

    def get_queryset(self):
        return Burial.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')

class BurialDetailView(DetailView):
    model = Burial

class BurialCreateView(CreateView):
    form_class = BurialForm
    model = Burial
class BurialDeleteView(DeleteView):
    model = Burial
    success_url = reverse_lazy('burial_list')


@login_required
def approve_burial(request,pk):
    burial = get_object_or_404(Burial, pk=pk)
    burial.approve()
    return redirect('assistance:burial_detail', pk=pk)

    
