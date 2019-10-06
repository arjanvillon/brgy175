from django.shortcuts import render

def skHome(request):
    return render(request, 'sk/skHome.html', {'title':'Sangguniang Kabataan'})