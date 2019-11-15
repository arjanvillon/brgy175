from django.urls import path
from vawc import views

app_name = 'vawc'

urlpatterns = [
    # path('', katarungan_views.katarunganHome, name='katarunganHome'),
	# path('dashboard/', katarungan_views.katarunganDashboard, name='katarunganDashboard'),
	# path('add/', katarungan_views.katarunganAddCase, name='katarunganAddCase'),

	path('',views.VawcListView.as_view(), name='list'),
	path('<int:pk>/', views.VawcDetailView.as_view(), name='detail'),
	path('create/', views.VawcCreateView.as_view(), name='create'),
	path('update/<int:pk>/', views.VawcUpdateView.as_view(), name='update'),
	path('delete/<int:pk>/', views.VawcDeleteView.as_view(), name='delete'),

]

