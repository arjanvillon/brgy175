from django.shortcuts import render
from .models import Resident
from residents.forms import ResidentForm
from katarungan.models import Katarungan
import datetime

from django.views.generic import (
    View, TemplateView,
    ListView, DetailView,
    CreateView, UpdateView,
    DeleteView
)

class ResidentListView(ListView):
    context_object_name = 'resident_list'
    model = Resident

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

class ResidentUpdateView(UpdateView):
    form_class = ResidentForm
    model = Resident


# from django.shortcuts import render, redirect
# from django.contrib import messages
# from .forms import ResidentBasicForm
# from .models import Resident

# def residentsHome(request):
#     data = Resident.objects.all
#     context = { 'data' : data, 'title':'Residents'}
#     return render(request, 'residents/residentsHome.html', context)

# def residentsAdd(request): 
#     form_res = ResidentBasicForm()  
#     if request.method == 'POST':
#         form_res = ResidentBasicForm(request.POST)
#         if form_res.is_valid():
#             form_res.save()
#             messages.success(request, 'Successfully registered!')
#             # age = form.cleaned_data['age']
#             # if age >=60:
#             #     # create senior id
#             # else:
#                 # ignore and don't create senior id  
#     else:
#          form_res = ResidentBasicForm()

#     context = {
#         'form_res': form_res
#     }

#     return render(request, 'residents/residentsAdd.html', context)



# def residentsView(request):
#     return render(request, 'residents/residentsView.html', {'title':'Residents'})

