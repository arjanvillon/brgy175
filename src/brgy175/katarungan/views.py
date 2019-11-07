from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import (View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)
# from katarungan.forms import CaseForm
from katarungan import models

class KatarunganListView(ListView):
    context_object_name = 'katarungans'
    model =  models.Katarungan

class KatarunganDetailView(DetailView):
    context_object_name = 'katarungan_detail'
    model = models.Katarungan
    template_name = 'katarungan/katarungan_detail.html'


# def katarunganHome(request):
#     data = Katarungan.objects.all()
#     context = { 'data': data, 'title':'Katarungang Pambarangay' }
#     return render(request, 'katarungan/katarunganHome.html' , context)

# def katarunganDashboard(request):
#     return render(request, 'katarungan/katarunganDashboard.html', {'title':'Katarungang Pambarangay Dashboard'})

# def katarunganAddCase(request):
#     form = CaseForm()
    
#     if request.method == 'POST':
#         form = CaseForm(request.POST)
#         if form.is_valid():
#             case = form.save()
#             return redirect('/katarunganHome/')
#     else:
#         form = CaseForm()

#     return render(request, 'katarungan/katarunganAdd.html', {'form':form})
