from django.shortcuts import render
from . import models
from residents.forms import ResidentForm
from django.views.generic import (
    View, TemplateView,
    ListView, DetailView,
    CreateView, UpdateView,
    DeleteView
)

class ResidentListView(ListView):
    context_object_name = 'resident_list'
    model = models.Resident

class ResidentDetailView(DetailView):
    context_object_name = 'resident_detail'
    model = models.Resident
    template_name = 'residents/resident_detail.html'

class ResidentCreateView(CreateView):
    form_class = ResidentForm
    # fields = ('first_name', 'middle_name', 'last_name', 'suffix', 'address', 'date_of_birth', 'place_of_birth', 'age', 'weight', 'height', 'gender', 'civil_status', 'contact_number', 'nationality', 'email_address', 'religion')
    model = models.Resident

class ResidentUpdateView(UpdateView):
    form_class = ResidentForm
    model = models.Resident


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

