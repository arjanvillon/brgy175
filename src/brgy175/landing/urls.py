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
    path('register/', views.ResidentCreateView.as_view(), name='landing_register'),
    path('apply/', views.landing_apply, name='apply'),
    path('id/create/', views.IdCreateView.as_view(), name='create_id'),
    path('indigency/create/', views.IndigencyCreateView.as_view(), name='create_indigent'),
    path('clearance/create/', views.ClearanceCreateView.as_view(), name='create_clearance'),
    path('scholarship/create/', views.ScholarshipCreateView.as_view(), name='create_scholar'),
    path('business/create/', views.BusinessCreateView.as_view(), name='create_business'),
    path('burial/create/', views.BurialCreateView.as_view(), name='create_burial'),
    path('id/update/<int:pk>/', views.IdUpdateView.as_view(), name='update_id'),
    path('indigency/update/<int:pk>/', views.IndigencyUpdateView.as_view(), name='update_indigent'),
    path('clearance/update/<int:pk>/', views.ClearanceUpdateView.as_view(), name='update_clearance'),
    path('scholarship/update/<int:pk>/', views.IdUpdateView.as_view(), name='update_scholar'),
    path('business/update/<int:pk>/', views.BusinessUpdateView.as_view(), name='update_business'),
    path('burial/update/<int:pk>/', views.BurialUpdateView.as_view(), name='update_burial'),
    path('id/detail/<int:pk>/', views.IdDetailView.as_view(), name='detail_id'),
    path('indigency/detail/<int:pk>/', views.IndigencyDetailView.as_view(), name='detail_indigent'),
    path('clearance/detail/<int:pk>/', views.ClearanceDetailView.as_view(), name='detail_clearance'),
    path('scholarship/detail/<int:pk>/', views.ScholarshipDetailView.as_view(), name='detail_scholar'),
    path('business/detail/<int:pk>/', views.BusinessDetailView.as_view(), name='detail_business'),
    path('burial/detail/<int:pk>/', views.BurialDetailView.as_view(), name='detail_burial'),
    


]
