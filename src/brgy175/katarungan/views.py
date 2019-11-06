from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CaseForm
from .models import Katarungan


def katarunganHome(request):
    data = Katarungan.objects.all()
    context = { 'data': data, 'title':'Katarungang Pambarangay' }
    return render(request, 'katarungan/katarunganHome.html' , context)

def katarunganDashboard(request):
    return render(request, 'katarungan/katarunganDashboard.html', {'title':'Katarungang Pambarangay Dashboard'})

def katarunganAddCase(request):
    form = CaseForm()
    
    if request.method == 'POST':
        form = CaseForm(request.POST)
        if form.is_valid():
            case = form.save()
            return redirect('/katarunganHome/')
    else:
        form = CaseForm()

    return render(request, 'katarungan/katarunganAdd.html', {'form':form})
