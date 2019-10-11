from django.urls import path
from . import views 
from user_account.views import logout_view

urlpatterns = [
	path('', views.homeBase, name='home'),
	path('logout/', logout_view, name = 'logout')
]