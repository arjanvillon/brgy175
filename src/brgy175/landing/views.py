from django.shortcuts import render, redirect
from django import forms
from django.db.models import Q
from residents.models import Resident
from .forms import FormId, FormIdigent, FormScholar, FormBurial, FormBusiness, FormClearance
from .models import IDForm, IndigencyForm, ClearanceForm, ScholarshipForm,BusinessPermit,BurialForm
from announcement.models import Announcement
from residents.forms import ResidentForm
import datetime
from django.views.generic import (
    View, TemplateView,
    ListView, DetailView,
    CreateView, UpdateView,
    DeleteView
)

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

#==========Residents form ===================


class ResidentDetailView(DetailView):
    context_object_name = 'resident_detail'
    model = Resident
    template_name = 'residents/resident_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cases"] =  Katarungan.objects.filter(convict__pk=self.kwargs['pk'])
        return context
    
class ResidentCreateView(CreateView):
    form_class = ResidentForm
    # fields = ('first_name', 'middle_name', 'last_name', 'suffix', 'address', 'date_of_birth', 'place_of_birth', 'age', 'weight', 'height', 'gender', 'civil_status', 'contact_number', 'nationality', 'email_address', 'religion')
    model = Resident
    template_name = "landing/landing_application.html"

    def get_context_data(self, **kwargs):
        query = Resident.objects.all().latest('created_date')
        if not query:
            senior_id = "S-2019-0000"
        else:
            pk = query.pk + 1
            year = datetime.datetime.now().year

            if pk < 10:
                senior_id = "S-" + str(year) + "-000" + str(pk)
            elif pk >= 10 and pk < 100:
                senior_id = "S-" + str(year) + "-00" + str(pk)
            elif pk >= 100 and pk < 1000:
                senior_id = "S-" + str(year) + "-0" + str(pk)
            else:
                senior_id = "S-" + str(year) + "-" + str(pk)

        pwd_query = Resident.objects.all().latest('created_date')
        if not pwd_query:
            pwd_id = "PWD-2019-0000"
        else:
            pk_pwd = pwd_query.pk + 1
            year = datetime.datetime.now().year

            if pk_pwd < 10:
                pwd_id = "PWD-" + str(year) + "-000" + str(pk_pwd)
            elif pk_pwd >= 10 and pk_pwd < 100:
                pwd_id = "PWD-" + str(year) + "-00" + str(pk_pwd)
            elif pk_pwd >= 100 and pk_pwd < 1000:
                pwd_id = "PWD-" + str(year) + "-0" + str(pk_pwd)
            else:
                pwd_id = "PWD-" + str(year) + "-" + str(pk_pwd)

        context = super().get_context_data(**kwargs)
        context["senior_id"] = senior_id
        context["pwd_id"] = pwd_id
        return context


class IdCreateView(CreateView):
    form_class = FormId
    model = IDForm
    template_name = 'landing/id_form.html'
    queryset = IDForm.objects.all() 


class IdUpdateView(UpdateView):
    form_class = FormId
    model = IDForm
    template_name = 'landing/id_form.html'
    queryset = IDForm.objects.all()

class IdDetailView(DetailView):
    form_class = FormId
    model = IDForm
    template_name = 'landing/id_form.html'
    queryset = IDForm.objects.all()  
    


class IndigencyCreateView(CreateView):
    form_class = FormIdigent
    model = IndigencyForm
    template_name = 'landing/indigency_form.html'
    queryset = IndigencyForm.objects.all() 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['indigent'] = self.get_form()
        return context

class IndigencyUpdateView(UpdateView):
    form_class = FormIdigent
    model = IndigencyForm
    template_name = 'landing/indigency_form.html'
    queryset = IndigencyForm.objects.all() 

class IndigencyDetailView(DetailView):
    form_class = FormIdigent
    model = IndigencyForm
    template_name = 'landing/indigency_form.html'
    queryset = IndigencyForm.objects.all() 

class ClearanceCreateView(CreateView):
    form_class = FormClearance
    model = ClearanceForm
    template_name = 'landing/clearance_form.html'
    queryset = ClearanceForm.objects.all() 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['clearance'] = self.get_form()
        return context
class ClearanceUpdateView(UpdateView):
    form_class = FormClearance
    model = ClearanceForm
    template_name = 'landing/clearance_form.html'
    queryset = ClearanceForm.objects.all() 

class ClearanceDetailView(DetailView):
    form_class = FormClearance
    model = ClearanceForm
    template_name = 'landing/clearance_form.html'
    queryset = ClearanceForm.objects.all() 

class ScholarshipCreateView(CreateView):
    form_class = FormScholar
    model = ScholarshipForm
    template_name = 'landing/scholar_form.html'
    queryset = IndigencyForm.objects.all() 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['scholar'] = self.get_form()
        return context

class ScholarshipUpdateView(UpdateView):
    form_class = FormScholar
    model = ScholarshipForm
    template_name = 'landing/scholar_form.html'
    queryset = IndigencyForm.objects.all() 

class ScholarshipDetailView(DetailView):
    form_class = FormScholar
    model = ScholarshipForm
    template_name = 'landing/scholar_form.html'
    queryset = IndigencyForm.objects.all() 

class BusinessCreateView(CreateView):
    form_class = FormBusiness
    model = BusinessPermit
    template_name = 'landing/business_form.html'
    queryset = IndigencyForm.objects.all() 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['business'] = self.get_form()
        return context

class BusinessUpdateView(UpdateView):
    form_class = FormBusiness
    model = BusinessPermit
    template_name = 'landing/business_form.html'
    queryset = IndigencyForm.objects.all() 

class BusinessDetailView(DetailView):
    form_class = FormBusiness
    model = BusinessPermit
    template_name = 'landing/business_form.html'
    queryset = IndigencyForm.objects.all() 

class BurialCreateView(CreateView):
    form_class = FormBurial
    model = BurialForm
    template_name = 'landing/burial_form.html'
    queryset = IndigencyForm.objects.all() 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['burial'] = self.get_form()
        return context

class BurialUpdateView(UpdateView):
    form_class = FormBurial
    model = BurialForm
    template_name = 'landing/burial_form.html'
    queryset = IndigencyForm.objects.all() 

class BurialDetailView(DetailView):
    form_class = FormBurial
    model = BurialForm
    template_name = 'landing/burial_form.html'
    queryset = IndigencyForm.objects.all() 
