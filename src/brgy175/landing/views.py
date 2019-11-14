from django.shortcuts import render, redirect
from django.db.models import Q
from residents.models import Resident
from .forms import FormId, FormIdigent, FormScholar, FormBurial, FormBusiness, FormClearance
from .models import IDForm, IndigencyForm

def landing_forms(request):
    id_form = FormId(prefix='a')
    form_idigent    =   FormIdigent(prefix='b')
    form_scholar    =   FormScholar()
    form_burial     =   FormBurial()
    form_business   =   FormBusiness()
    form_clearance  =   FormClearance()
    q_id = ""
    obj_id = 0
    context = {
            'form':id_form,
            'indigent':  form_idigent,
            'scholar':  form_scholar,
            'burial' :  form_burial,
            'business': form_business,
            'clearance': form_clearance,
            
        }
    
    if request.GET:
        query = request.GET.get('search_name')
        residents_query = []
        split_queries = query.split(" ")
        for q in split_queries:
            filter_query = Resident.objects.filter(
                Q(first_name__icontains=q)|
                Q(middle_name__icontains=q)|
                Q(last_name__icontains=q)|
                Q(email_address__icontains=q)
            ).distinct()

            for qs in filter_query:
                residents_query.append(qs)
            resident_list = list(set(residents_query))

        length_list = len(resident_list)
        if length_list > 1 or length_list < 1:
            print(resident_list)
            context = {
                'form':id_form,
                'indigent':  form_idigent,
                'scholar':  form_scholar,
                'burial' :  form_burial,
                'business': form_business,
                'clearance': form_clearance,
            }
        else:
            q_id = resident_list[0]
            obj_id = q_id.id
            print(str(obj_id))
            
            if IDForm.objects.filter(resident_idform=obj_id).exists():
                id_model = IDForm.objects.get(resident_idform=obj_id)
                id_form = FormId(instance=id_model)
                indigent_model = IndigencyForm.objects.get(resident_indigency=obj_id)
                form_idigent = FormIdigent(instance=indigent_model)


                context = {
                    'obj_result':q_id,
                    'value':obj_id,
                    'form':id_form,
                    'id_model': id_model,
                    'indigent':  form_idigent,
                    'scholar':  form_scholar,
                    'burial' :  form_burial,
                    'business': form_business,
                    'clearance': form_clearance,
                }
            else:
                context = {
                    'obj_result':q_id,
                    'value':obj_id,
                    'form':id_form,
                    'indigent':  form_idigent,
                    'scholar':  form_scholar,
                    'burial' :  form_burial,
                    'business': form_business,
                    'clearance': form_clearance,
                }
                

            if request.method == 'POST':
                id_form = FormId(request.POST, prefix='a')
                form_idigent = FormIdigent(request.POST, prefix='b')
                form_scholar = FormScholar(request.POST, prefix='c')
                form_burial = FormBurial(request.POST, prefix='d')
                form_business = FormBusiness(request.POST, prefix='e')
                form_clearance = FormClearance(request.POST, prefix='f')
                if id_form.is_valid():
                    id_form.cleaned_data['resident_idform'] = obj_id
                    a = id_form.save()
                if form_idigent.is_valid():
                    form_idigent.cleaned_data['resident_indigency'] = obj_id
                    b = form_idigent.save()
                if form_scholar.is_valid():
                    form_scholar.cleaned_data['resident_scholar'] = obj_id
                    c = form_scholar.save()
                if form_burial.is_valid():
                    form_burial.cleaned_data['resident_burial'] = obj_id
                    d = form_burial.save()
                if form_business.is_valid():
                    form_business.cleaned_data['resident_business'] = obj_id
                    e = form_business.save()
                if form_clearance.is_valid():
                    form_clearance.cleaned_data['resident_clearance'] = obj_id
                    f = form_clearance.save()
                # if 'Submit_id' in request.POST:
                #     post_values = request.POST.copy()
                #     post_values['resident_idform'] = obj_id
                #     print(str(post_values))
                #     id_form = FormId(post_values)
                #     if id_form.is_valid():
                #         id_form.save()             
                # elif  'Submit_indigent' in request.POST:
                #     post_values = request.POST
                #     print(str(post_values))
                #     post_values['resident_indigency'] = obj_id
                #     form_idigent    =   FormIdigent(post_values)
                #     print(str(form_idigent))
                #     if form_idigent.is_valid():
                #         form_idigent.save()
                # elif  'Submit_scholar' in request.POST:
                #     post_values = request.POST.copy()
                #     post_values['resident_scholarship'] = obj_id
                #     print(str(post_values))
                #     form_scholar    =   FormScholar(post_values)
                #     if form_scholar.is_valid():
                #         form_scholar.save()
                # elif  'Submit_burial' in request.POST:
                #     post_values = request.POST.copy()
                #     post_values['resident_burial'] = obj_id
                #     print(str(post_values))
                #     form_burial =  FormBurial(post_values)
                #     if form_burial.is_valid():
                #         form_burial.save()
                # elif  'Submit_business' in request.POST:
                #     post_values = request.POST.copy()
                #     post_values['resident_business'] = obj_id
                #     print(str(post_values))
                #     form_business   =   FormBusiness(post_values)
                #     if form_business.is_valid():
                #         form_business.save()
                # elif  'Submit_clearance' in request.POST:
                #     post_values = request.POST.copy()
                #     post_values['resident_clearance'] = obj_id
                #     print(str(post_values))
                #     form_clearance  =   FormClearance(post_values)
                #     if form_clearance.is_valid():
                #         form_clearance.save()

                
                
                else:
                    
                    context = {
                        'obj_result':q_id,
                        'value':obj_id,
                        'form':id_form,
                        'indigent':  form_idigent,
                        'scholar':  form_scholar,
                        'burial' :  form_burial,
                        'business': form_business,
                        'clearance': form_clearance,
                    }
            

    
        
    return render(request, 'landing/form_landing.html', context)

def landing_id_form(request):
    
    return render(request, 'landing/form_landing.html', context)



def landing_base(request):
    return render(request, 'landing/landing_base.html')

def about_us(request):
    return render(request, 'landing/about_us.html')

def contact(request):
    return render(request, 'landing/contact.html')

# class ContactView(TemplateView):
#     template_name = 'landing/contact.html'






