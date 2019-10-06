from django.urls import path
from . import views

urlpatterns = [
    path('', views.residentsHome, name="residentsHome"),
    path('add/', views.residentsAdd, name="residentsAdd"),
    path('view/', views.residentsView, name="residentsView"),
    path('view/scholarship/', views.residentsViewScholarship, name="residentsViewScholarship"),
    path('view/cases/', views.residentsViewCases, name="residentsViewCases"),
]
