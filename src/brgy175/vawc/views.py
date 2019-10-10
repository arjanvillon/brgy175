from django.shortcuts import render
from .forms import CaseForm
from .models import vawc
from user_account.decorators import superadmin_vawc_only

@superadmin_vawc_only
def vawcHome(request):
    data = vawc.objects.all
    context = { 'data' : data, 'title':'VAWC'}
    return render(request, 'vawc/vawcHome.html', context)

def vawcAddCase(request):
    form = CaseForm()
    if request.method == 'POST':
        form = CaseForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CaseForm()

    context = {
        'form_case': form
    }

    return render(request, 'vawc/vawcAdd.html', context)
