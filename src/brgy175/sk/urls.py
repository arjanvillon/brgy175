from django.urls import path
from . import views

urlpatterns = [
    path('', views.skHome, name='skHome')
]