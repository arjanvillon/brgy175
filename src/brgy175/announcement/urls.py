from django.urls import path
from announcement import views

app_name = 'announcement'

urlpatterns = [
    path('', views.AnnouncementListView.as_view(), name='announcement_list'),
    path('<int:pk>/', views.AnnouncementDetailView.as_view(), name='announcement_detail'),
    path('create/', views.AnnouncementCreateView.as_view(), name='announcement_create'),
    path('<int:pk>/update/', views.AnnouncementUpdateView.as_view(), name='announcement_update'),
    path('<int:pk>/delete/', views.AnnouncementDeleteView.as_view(), name='announcement_delete'),
]

