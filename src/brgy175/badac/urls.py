from django.urls import path
from . import views

app_name = 'badac'

urlpatterns = [

	path('', views.BADACListView.as_view(), name='list'),
	path('<int:pk>/', views.BADACDetailView.as_view(), name='detail'),
	path('create/', views.BADACCreateView.as_view(), name='create'),
	path('update/<int:pk>/settle', views.settle_case, name='settle'),
	path('update/<int:pk>/withdraw', views.withdraw_case, name='withdraw'),
	path('delete/<int:pk>/', views.BADACDeleteView.as_view(), name='delete'),

]

