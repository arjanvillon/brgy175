from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ResidentBasicForm
from .models import Resident

def residentsHome(request):
    data = Resident.objects.all
    context = { 'data' : data, 'title':'Residents'}
    return render(request, 'residents/residentsHome.html', context)

def residentsAdd(request): 
    form_res = ResidentBasicForm()  
    if request.method == 'POST':
        form_res = ResidentBasicForm(request.POST)
        if form_res.is_valid():
            form_res.save()
    else:
         form_res = ResidentBasicForm()

    context = {
        'form_res': form_res
    }

    messages.success(request, 'Successfully registered!')  
    return render(request, 'residents/residentsAdd.html', context)



def residentsView(request):
    return render(request, 'residents/residentsView.html', {'title':'Residents'})

