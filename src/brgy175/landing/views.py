from django.shortcuts import render, redirect
from django import forms
from django.db.models import Q
from residents.models import Resident
from .forms import FormId, FormIdigent, FormScholar, FormBurial, FormBusiness, FormClearance
from .models import IDForm, IndigencyForm
from announcement.models import Announcement
from django.views.generic import (TemplateView, ListView, DetailView)

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
            
            if IDForm.objects.filter(resident=obj_id).exists():
                id_model = IDForm.objects.get(resident=obj_id)
                id_form = FormId(instance=id_model)
            if IndigencyForm.objects.filter(resident=obj_id).exists():
                indigent_model = IndigencyForm.objects.get(resident=obj_id)
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
        post_data = request.POST.copy()
        post_data['a-resident'] = obj_id
        id_form = FormId(post_data, prefix='a')
        print("this id: " + str(post_data))
        print("this form: " + str(id_form))
        form_idigent = FormIdigent(request.POST, prefix='b')
        form_scholar = FormScholar(request.POST, prefix='c')
        form_burial = FormBurial(request.POST, prefix='d')
        form_business = FormBusiness(request.POST, prefix='e')
        form_clearance = FormClearance(request.POST, prefix='f')
        if id_form.is_valid():
            id_form.cleaned_data['resident'] = obj_id
            a = id_form.save(commit=False)
            a = id_form.save()
        elif form_idigent.is_valid():
            form_idigent.cleaned_data['resident'] = obj_id
            b = form_idigent.save()
        elif form_scholar.is_valid():
            form_scholar.cleaned_data['resident'] = obj_id
            c = form_scholar.save()
        elif form_burial.is_valid():
            form_burial.cleaned_data['resident'] = obj_id
            d = form_burial.save()
        elif form_business.is_valid():
            form_business.cleaned_data['resident'] = obj_id
            e = form_business.save()
        elif form_clearance.is_valid():
            form_clearance.cleaned_data['resident'] = obj_id
            f = form_clearance.save()
        # if 'Submit_id' in request.POST:
        #     post_values = request.POST.copy()
        #     post_values['resident_idform'] = obj_id
        #     print(str(post_values))
        #     id_form = FormId(post_values)
        #     if id_form.is_valid():
        #         id_form.save()          

        
        
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

def landing_apply(request):
    return render(request, 'landing/landing_application.html')

def landing_base(request):
    return render(request, 'landing/landing_base.html')

def about_us(request):
    return render(request, 'landing/about_us.html')

def contact(request):
    return render(request, 'landing/contact.html')

# def landing_announce(request):
#     announce = Announcement.objects.all

#     context = {
#         'announcement':announce
#     }

#     return render(request, 'landing/landing_announcements.html', context)

class AnnouncementDetailView(DetailView):
    template_name = "landing/landing_announcements_detail.html"
    model = Announcement

class AnnouncementListView(ListView):
    template_name = "landing/landing_announcements.html"

    model = Announcement
    
    def get_queryset(self):
        return Announcement.objects.all().order_by('-created_date')






