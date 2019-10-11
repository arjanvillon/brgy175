from django.shortcuts import render
import datetime
from django.utils.timezone import utc

def base(request):
    return render(request, 'home/base.html', {'title':'Dashboard'})

def homeBase(request):
    return render(request, 'home/dashboard.html', {'title':'Dashboard'})


