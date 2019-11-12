from django.shortcuts import render
from .forms import Form_id, Form_idigent, Form_business, Form_clearance
def landing_forms(request):
    form_id       =    Form_id()
    form_idigent    =   Form_idigent()
    # form_scholar    =   Form_scholar()
    # form_burial     =   Form_burial()
    form_business   =   Form_business()
    form_clearance  =   Form_clearance()
    if request.method == 'POST':
        if 'Submit_id' == request.POST:
            
            form_id =  Form_id(request.POST)
            if form_id.is_valid():
                print("True"+ str(form_id))
                form_id.save()
        if 'Submit_indigent' == request.POST:
            form_idigent    =   Form_idigent(request.POST)
            if form_idigent.is_valid():
                form_idigent.save()
        # if 'Submit_scholar' == request.POST:
        #     form_scholar    =   Form_scholar(request.POST)
        #     if form_scholar.is_valid():
        #         form_scholar.save()
        # if 'Submit_burial' == request.POST:
        #     form_burial =  Form_burial(request.POST)
        #     if form_burial.is_valid():
        #         form_burial.save()
        if 'Submit_business' == request.POST:
            form_business   =   Form_business(request.POST)
            if form_business.is_valid():
                form_business.save()
        if 'Submit_clearance' == request.POST:
            form_clearance  =   Form_clearance(request.POST)
            if form_clearance.is_valid():
                form_clearance.save()
    else:
        form_id        =   Form_id()
        form_idigent    =   Form_idigent()
        # form_scholar    =   Form_scholar()
        # form_burial     =   Form_burial()
        form_business   =   Form_business()
        form_clearance  =   Form_clearance()
    
    context = {
        'form'   :  Form_id(),
        'indigent':  form_idigent,
        # 'scholar':  form_scholar,
        # 'burial' :  form_burial,
        'business': form_business,
        'clearance': form_clearance,
    }
    

    return render(request, 'landing/form_landing.html', context)

def landing_base(request):
    return render(request, 'landing/landing_base.html')

def about_us(request):
    return render(request, 'landing/about_us.html')

def contact(request):
    return render(request, 'landing/co.html')






