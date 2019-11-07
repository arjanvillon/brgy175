from django.shortcuts import render
from .models import badac

def badacHome(request):
     data = badac.objects.all
     context = { 'data' : data, 'title':'BADAC' }
     return render(request, 'badac/badacHome.html' , context)