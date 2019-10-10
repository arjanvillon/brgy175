from django.shortcuts import render
from residents.models import Resident
from user_account.decorators import superadmin_senior_only

@superadmin_senior_only
def seniorHome(request):
    data = Resident.objects.all
    context = { 'data' : data, 'title':'PWD & Senior Department'}
    return render(request, 'senior/seniorHome.html', context) 