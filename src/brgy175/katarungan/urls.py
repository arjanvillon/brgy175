from django.urls import path
from . import views

urlpatterns = [
	path('', views.katarunganHome, name='katarunganHome'),
	path('dashboard', views.katarunganDashboard, name='katarunganDashboard'),

]