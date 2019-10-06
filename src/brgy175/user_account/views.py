from django.shortcuts import render
from .forms import UserRegisterForm 


# Create your views here.

def login(request):
    return render(request, 'user_account/login.html')

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)

		if form.is_valid():
			form.save()

			
	else:	
		form = UserRegisterForm()
	return render(request, 'user_account/login.html',{ 'form':form})
