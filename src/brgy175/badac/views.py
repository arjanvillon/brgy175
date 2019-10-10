from django.shortcuts import render
from .models import badac
from user_account.decorators import superadmin_badac_only

@superadmin_badac_only
def badacHome(request):
     data = badac.objects.all
     context = { 'data' : data, 'title':'BADAC' }
     return render(request, 'badac/badacHome.html' , context)