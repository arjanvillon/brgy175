from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (View, TemplateView, ListView, DetailView, CreateView, DeleteView)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from katarungan.models import Katarungan
import datetime

class KatarunganTemplateView(TemplateView):
    template_name = "reports/katarungan_reports.html"
    model = Katarungan

    def get_context_data(self, **kwargs):
        date = datetime.datetime.now()
        month = date.strftime("%B").upper()

        context = super().get_context_data(**kwargs)
        context["month"] = month
        return context
    