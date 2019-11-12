from django.urls import path
from residents import views

app_name = 'residents'

urlpatterns = [
    path('', views.ResidentListView.as_view(), name='resident_list'),
	path('<int:pk>/', views.ResidentDetailView.as_view(), name='resident_detail'),
	path('add/', views.ResidentCreateView.as_view(), name='add_resident'),
	path('update/<int:pk>/', views.ResidentUpdateView.as_view(), name='update'),
]