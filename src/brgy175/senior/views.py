from django.shortcuts import render

def seniorHome(request):
    return render(request, 'senior/seniorHome.html', {'title':'PWD & Senior Department'})