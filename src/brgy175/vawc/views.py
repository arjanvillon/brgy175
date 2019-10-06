from django.shortcuts import render

def vawcHome(request):
    return render(request, 'vawc/vawcHome.html', {'title':'VAWC'})