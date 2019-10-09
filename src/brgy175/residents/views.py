from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ResidentBasicForm

def residentsHome(request):
    return render(request, 'residents/residentsHome.html', {'title':'Residents'})

def residentsAdd(request):
    if request.method == 'POST':
        form_res = ResidentBasicForm(request.POST)

        if form_res.is_valid():
            form_res.save()


    else:
        form_res = ResidentBasicForm()
    context = {
        'form_res': form_res
    }
    return render(request, 'residents/residentsAdd.html', context)



def residentsView(request):
    return render(request, 'residents/residentsView.html', {'title':'Residents'})

