from django.urls import path
from . import views

app_name = 'reports'

urlpatterns = [

    path('', views.KatarunganTemplateView.as_view(), name='katarungan_reports'),

]

