from django.urls import path
from . import views

app_name = 'assistance'

urlpatterns = [
	path('', views.Assistance.as_view(), name='assistance'),

	# Scholar Assistance URLs
	path('scholar/', views.ScholarListView.as_view(), name='scholar_list'),
	path('scholar/<int:pk>', views.ScholarDetailView.as_view(), name='scholar_detail'),
	path('scholar/create/', views.ScholarCreateView.as_view(), name='scholar_create'),
	path('scholar/<int:pk>/delete/', views.ScholarDeleteView.as_view(), name='scholar_delete'),
	path('scholar/<int:pk>/approve/', views.approve_scholar, name='approve_scholar'),

	# Burial Assistance URLs
	path('burial/', views.BurialListView.as_view(), name='burial_list'),
	path('burial/<int:pk>', views.BurialDetailView.as_view(), name='burial_detail'),
	path('burial/create/', views.BurialCreateView.as_view(), name='burial_create'),
	path('burial/<int:pk>/delete/', views.BurialDeleteView.as_view(), name='burial_delete'),
	path('burial/<int:pk>/approve/', views.approve_burial, name='approve_burial'),
]