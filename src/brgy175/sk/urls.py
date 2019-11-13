from django.urls import path
from . import views

app_name = 'sk'

urlpatterns = [
	path('', views.SkHomeView.as_view(), name='sk-home'),
]