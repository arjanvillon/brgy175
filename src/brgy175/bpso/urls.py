from django.urls import path
from . import views

app_name = 'bpso'

urlpatterns = [

	path('', views.BPSOListView.as_view(), name='list'),
	path('<int:pk>/', views.BPSODetailView.as_view(), name='detail'),
	path('create/', views.BPSOCreateView.as_view(), name='create'),
	path('update/<int:pk>/settle', views.settle_case, name='settle'),
	path('update/<int:pk>/withdraw', views.withdraw_case, name='withdraw'),
	path('delete/<int:pk>/', views.BPSODeleteView.as_view(), name='delete'),

]

