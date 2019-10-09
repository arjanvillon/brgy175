from django.shortcuts import render
from django.contrib import messages
from .forms import CaseForm

def katarunganHome(request):
    return render(request, 'katarungan/katarunganHome.html' , {'title':'Katarungang Pambarangay'})

def katarunganDashboard(request):
    return render(request, 'katarungan/katarunganDashboard.html', {'title':'Katarungang Pambarangay Dashboard'})

def katarunganAddCase(request):
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

    messages.success(request, 'Successfully filed a case!')  
    return render(request, 'katarungan/katarunganAdd.html', context)


