from django.shortcuts import render
from residents.models import Resident

from django.views.generic import TemplateView

class SeniorIndexView(TemplateView):
    template_name = 'senior/senior_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["senior"] = Resident.objects.filter(is_senior="Senior").all()
        return context
    
class PwdIndexView(TemplateView):
    template_name = 'senior/pwd_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pwd"] = Resident.objects.filter(is_pwd="yes").all()
        return context