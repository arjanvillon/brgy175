from django.urls import path
from . import views

urlpatterns = [
	path('', views.assistanceHome, name='assistanceHome'),
]