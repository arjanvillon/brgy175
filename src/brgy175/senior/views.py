from django.shortcuts import render
from residents.models import Resident

def seniorHome(request):
    data = Resident.objects.all
    context = { 'data' : data, 'title':'PWD & Senior Department'}
    return render(request, 'senior/seniorHome.html', context) 

def senior(request):
    data = Resident.objects.all
    context = { 'data' : data, 'title':'PWD & Senior Department'}
    return render(request, 'senior/senior.html', context) 

def pwd(request):
    data = Resident.objects.all
    context = { 'data' : data, 'title':'PWD & Senior Department'}
    return render(request, 'senior/pwd.html', context) 