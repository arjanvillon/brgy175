from django.urls import path
from sk import views

app_name = 'sk'

urlpatterns = [
	path('', views.SkHomeView.as_view(), name='sk-home'),
	path('list/', views.SkListView.as_view(), name='sk_list'),
	path('create/', views.SkCreateView.as_view(), name='sk_create'),
	path('<int:pk>/', views.SkDetailView.as_view(), name='sk_detail'),
	path('update/<int:pk>/', views.SkUpdateView.as_view(), name='sk_update'),
] 