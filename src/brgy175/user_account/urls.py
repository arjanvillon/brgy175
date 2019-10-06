from django.urls import path, include
from . import views 

urlpatterns = [
	path('', views.login, name="user_account"),
	path('home/', include('home.urls')),


]