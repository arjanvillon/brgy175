from django.shortcuts import render
from .forms import CaseForm
from .models import bpso

def bpsoHome(request):
     data = bpso.objects.all
     context = { 'data' : data, 'title':'BPSO'}
     return render(request, 'bpso/bpsoHome.html' ,context)



def bpsoAddCase(request):
    form = CaseForm()
    if request.method == 'POST':
        form = CaseForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CaseForm()

    context = {
        'form_case': form
    }

    return render(request, 'bpso/bpsoHome.html' , context)