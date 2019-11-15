from django.urls import path
from landing import views


app_name = 'landing'

urlpatterns = [
    path('forms/', views.landing_forms, name='landingForms'),
    path('', views.landing_base, name='landingBase'),
    path('about/',views.about_us, name='aboutUs'),
    path('contact/',views.contact, name='contactUs'),
    path('announcement/', views.AnnouncementListView.as_view(), name='landing_announcement_list'),
    path('announcement/<int:pk>/', views.AnnouncementDetailView.as_view(), name='announcement_detail'),
    path('apply/', views.landing_apply, name='apply'),


]
