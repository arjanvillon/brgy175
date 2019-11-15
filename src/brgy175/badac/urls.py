from django.urls import path
from . import views

app_name = 'badac'

urlpatterns = [

	path('', views.BADACListView.as_view(), name='list'),
	path('<int:pk>/', views.BADACDetailView.as_view(), name='detail'),
	path('create/', views.BADACCreateView.as_view(), name='create'),
	path('update/<int:pk>/R', views.R_case, name='R'),
	path('update/<int:pk>/G', views.G_case, name='G'),
	path('update/<int:pk>/B', views.B_case, name='B'),
	path('update/<int:pk>/Y', views.Y_case, name='Y'),
	path('delete/<int:pk>/', views.BADACDeleteView.as_view(), name='delete'),

]

