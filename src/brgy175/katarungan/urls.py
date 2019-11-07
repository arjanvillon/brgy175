from django.urls import path
from katarungan import views

app_name = 'katarungan'

urlpatterns = [
    # path('', katarungan_views.katarunganHome, name='katarunganHome'),
	# path('dashboard/', katarungan_views.katarunganDashboard, name='katarunganDashboard'),
	# path('add/', katarungan_views.katarunganAddCase, name='katarunganAddCase'),

	path('', views.KatarunganListView.as_view(), name='list'),
	path('<int:pk>/', views.KatarunganDetailView.as_view(), name='detail'),
	path('create/', views.KatarunganCreateView.as_view(), name='create'),
	path('update/<int:pk>/', views.KatarunganUpdateView.as_view(), name='update'),
	path('delete/<int:pk>/', views.KatarunganDeleteView.as_view(), name='delete'),

]

