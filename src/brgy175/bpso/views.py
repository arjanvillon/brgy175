from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic import (View, TemplateView, ListView, DetailView, CreateView, DeleteView)
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import FormBPSO
from .forms import FormBPSOForm
import datetime

class BPSOListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    context_object_name = 'bpso_list'
    model = FormBPSO

class BPSODetailView(LoginRequiredMixin, DetailView):
    login_url = '/login/'
    context_object_name = 'bpso_detail'
    model = FormBPSO
    template_name = 'bpso/formbpso_detail.html'

class BPSOCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    form_class = FormBPSOForm
    model = FormBPSO

    def get_context_data(self, **kwargs):
        try:
            query = FormBPSO.objects.all().latest('created_date')
        except FormBPSO.DoesNotExist:
            query = None

        if not query:
            case_no_bpso = "BPSO-2019-0000"
        else:
            pk = query.pk + 1
            year = datetime.datetime.now().year

            if pk < 10:
                case_no_bpso = "BPSO-" + str(year) + "-000" + str(pk)
            elif pk >= 10 and pk < 100:
                case_no_bpso = "BPSO-" + str(year) + "-00" + str(pk)
            elif pk >= 100 and pk < 1000:
                case_no_bpso = "BPSO-" + str(year) + "-0" + str(pk)
            else:
                case_no_bpso = "BPSO-" + str(year) + "-" + str(pk)

        context = super().get_context_data(**kwargs)
        context["latest_pk"] = case_no_bpso
        return context

class BPSODeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    model = FormBPSO
    success_url = reverse_lazy('bpso:list')


@login_required
def cfa_case(request, pk):
    case = get_object_or_404(FormBPSO, pk=pk)
    case.cfa()
    return redirect('bpso:detail', pk=pk)


@login_required
def settle_case(request, pk):
    case = get_object_or_404(FormBPSO, pk=pk)
    case.settle()
    return redirect('bpso:detail', pk=pk)

@login_required
def withdraw_case(request, pk):
    case = get_object_or_404(FormBPSO, pk=pk)
    case.withdraw()
    return redirect('bpso:detail', pk=pk)

