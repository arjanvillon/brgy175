from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic import (View, TemplateView, ListView, DetailView, CreateView, DeleteView)
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from user_account.decorators import superadmin_katarungan_only
from .models import Katarungan
from .forms import KatarunganForm
import datetime

class KatarunganListView(LoginRequiredMixin, superadmin_katarungan_only, ListView):
    login_url = '/login/'
    context_object_name = 'katarungans'
    model = Katarungan

class KatarunganDetailView(LoginRequiredMixin,superadmin_katarungan_only, DetailView):
    login_url = '/login/'
    context_object_name = 'katarungan_detail'
    model = Katarungan
    template_name = 'katarungan/katarungan_detail.html'

class KatarunganCreateView(LoginRequiredMixin,superadmin_katarungan_only, CreateView):
    login_url = '/login/'
    form_class = KatarunganForm
    model = Katarungan

    def get_context_data(self, **kwargs):
        query = Katarungan.objects.all().latest('created_date')
        if not query:
            case_no = "K-2019-0000"
        else:
            pk = query.pk + 1
            year = datetime.datetime.now().year

            if pk < 10:
                case_no = "K-" + str(year) + "-000" + str(pk)
            elif pk >= 10 and pk < 100:
                case_no = "K-" + str(year) + "-00" + str(pk)
            elif pk >= 100 and pk < 1000:
                case_no = "K-" + str(year) + "-0" + str(pk)
            else:
                case_no = "K-" + str(year) + "-" + str(pk)

        context = super().get_context_data(**kwargs)
        context["latest_pk"] = case_no
        return context

class KatarunganDeleteView(LoginRequiredMixin,superadmin_katarungan_only, DeleteView):
    login_url = '/login/'
    model = Katarungan
    success_url = reverse_lazy('katarungan:list')

@login_required
def settle_case(request, pk):
    case = get_object_or_404(Katarungan, pk=pk)
    case.settle()
    return redirect('katarungan:detail', pk=pk)

@login_required
def withdraw_case(request, pk):
    case = get_object_or_404(Katarungan, pk=pk)
    case.withdraw()
    return redirect('katarungan:detail', pk=pk)

