from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic import (View, TemplateView, ListView, DetailView, CreateView, DeleteView)
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import FormBADAC
from .forms import FormBADACForm
import datetime

class BADACListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    context_object_name = 'badac_list'
    model = FormBADAC

class BADACDetailView(LoginRequiredMixin, DetailView):
    login_url = '/login/'
    context_object_name = 'badac_detail'
    model = FormBADAC
    template_name = 'badac/formbadac_detail.html'

class BADACCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    form_class = FormBADACForm
    model = FormBADAC

    def get_context_data(self, **kwargs):
        query = FormBADAC.objects.all().latest('created_date')
        if not query:
            case_no_badac = "BADAC-2019-0000"
        else:
            pk = query.pk + 1
            year = datetime.datetime.now().year

            if pk < 10:
                case_no_badac = "BADAC-" + str(year) + "-000" + str(pk)
            elif pk >= 10 and pk < 100:
                case_no_badac = "BADAC-" + str(year) + "-00" + str(pk)
            elif pk >= 100 and pk < 1000:
                case_no_badac = "BADAC-" + str(year) + "-0" + str(pk)
            else:
                case_no_badac = "BADAC-" + str(year) + "-" + str(pk)

        context = super().get_context_data(**kwargs)
        context["latest_pk"] = case_no_badac
        return context

class BADACDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    model = FormBADAC
    success_url = reverse_lazy('badac:list')

@login_required
def settle_case(request, pk):
    case = get_object_or_404(FormBADAC, pk=pk)
    case.settle()
    return redirect('badac:detail', pk=pk)

@login_required
def withdraw_case(request, pk):
    case = get_object_or_404(FormBADAC, pk=pk)
    case.withdraw()
    return redirect('badac:detail', pk=pk)

