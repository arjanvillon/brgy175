from django.urls import path
from senior import views

app_name = 'senior'

urlpatterns = [
    path('', views.SeniorIndexView.as_view(), name='senior_list'),
    path('<int:pk>/', views.SeniorDetailView.as_view(), name='senior_detail'),
]
