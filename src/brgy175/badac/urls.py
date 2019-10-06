from django.urls import path
from . import views

urlpatterns = [
    path('', views.badacHome, name='badacHome')
]