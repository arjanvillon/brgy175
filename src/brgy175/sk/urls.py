from django.urls import path
from sk import views

app_name = 'sk'

urlpatterns = [
	# Home
	path('', views.SkHomeView.as_view(), name='sk-home'),
	# Project
	path('project/list/', views.ProjectListView.as_view(), name='project_list'),
	path('project/create/', views.ProjectCreateView.as_view(), name='project_create'),
	path('project/<int:pk>/', views.ProjectDetailView.as_view(), name='project_detail'),
	path('project/update/<int:pk>/', views.ProjectUpdateView.as_view(), name='project_update'),
	path('project/delete/<int:pk>/', views.ProjectDeleteView.as_view(), name='project_delete'),
] 