from django.shortcuts import render

def katarunganHome(request):
    return render(request, 'katarungan/katarunganHome.html' , {'title':'Katarungang Pambarangay'})

def katarunganDashboard(request):
    return render(request, 'katarungan/katarunganDashboard.html', {'title':'Katarungang Pambarangay Dashboard'})

