from django.urls import path
from . import views

app_name = 'katarungan'

urlpatterns = [

	path('', views.KatarunganListView.as_view(), name='list'),
	path('<int:pk>/', views.KatarunganDetailView.as_view(), name='detail'),
	path('create/', views.KatarunganCreateView.as_view(), name='create'),
	path('update/<int:pk>/cfa', views.cfa_case, name='cfa'),
	path('update/<int:pk>/settle', views.settle_case, name='settle'),
	path('update/<int:pk>/withdraw', views.withdraw_case, name='withdraw'),
	path('delete/<int:pk>/', views.KatarunganDeleteView.as_view(), name='delete'),

]

