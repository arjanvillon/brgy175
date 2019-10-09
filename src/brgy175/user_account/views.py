from django.shortcuts import render, redirect
from .forms import UserRegisterForm, LoginForm
from django.contrib.auth import authenticate, login
from django.conf import settings
from django.contrib.auth import logout
from django.contrib import messages


# Create your views here.

def register(request):
	if request.method == 'POST':
		if 'SignUp' in request.POST:
			
			form_register = UserRegisterForm(request.POST)
			if form_register.is_valid():
				form_register.save()

		elif 'SignIn' in request.POST:
			
			form_login = LoginForm(request.POST)
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					login(request, user)
					return redirect((settings.LOGIN_REDIRECT_URL))
			else:
				messages.error(request, 'username or password not correct')
				return redirect('/login/')
			
			context = {
				'form_l': form_login,
				'form_r': form_register,
			}
	else:	
		form_register = UserRegisterForm()
		form_login = LoginForm()

	context = {
		'form_l': form_login,
		'form_r': form_register,
	}
	
	return render(request, 'user_account/login.html', context)

def logout_view(request):
	logout(request)
	return redirect('/login/')

def userProfile(request):
	return render(request, 'user_account/profile.html', {'title': 'Profile'})

def updateProfile(request):
	return render(request, 'user_account/updateProfile.html', {'title': 'Update Profile'})



