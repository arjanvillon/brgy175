from django.shortcuts import render

def bpsoHome(request):
    return render(request, 'bpso/bpsoHome.html', {'title':'BPSO'})
