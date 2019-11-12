from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import (View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.urls import reverse_lazy
from .models import Katarungan
from .forms import KatarunganForm

class KatarunganListView(ListView):
    context_object_name = 'katarungans'
    model = Katarungan

class KatarunganDetailView(DetailView):
    context_object_name = 'katarungan_detail'
    model = Katarungan
    template_name = 'katarungan/katarungan_detail.html'

class KatarunganCreateView(CreateView):
    form_class = KatarunganForm
    model = Katarungan

    def get_context_data(self, **kwargs):
        query = Katarungan.objects.all().latest('created_date')
        pk = query.pk + 1
        year = query.created_date.year

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

class KatarunganUpdateView(UpdateView):
    fields = ('case_type', 'case_status')
    model = Katarungan

class KatarunganDeleteView(DeleteView):
    model = Katarungan
    success_url = reverse_lazy('katarungan:list')
