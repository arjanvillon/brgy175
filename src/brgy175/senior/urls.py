from django.urls import path
from senior import views

app_name = 'senior'

urlpatterns = [
    path('', views.SeniorIndexView.as_view(), name='senior_list'),
    path('pwd/', views.PwdIndexView.as_view(), name='pwd_list'),
]
