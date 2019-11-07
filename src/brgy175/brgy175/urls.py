"""brgy175 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf.urls.static import static
from landing import views as landing_views
from assistance import views as assistance_views
from badac import views as badac_views
from bpso import views as bpso_views
# from katarungan import views as katarungan_views
from residents import views as residents_views
from senior import views as senior_views
from sk import views as sk_views
from user_account import views as user_views
from vawc import views as vawc_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    path('login/', include('user_account.urls')),
    path('logout/', include('user_account.urls')),
    
    #SECTION landing URLs
    # path('', landing_views.index, name='index' ),
    # path('landing/projects', landing_views.landingProjects, name='landingProjects'),
    path('landing/forms', landing_views.landing_forms, name='landingForms'),
    path('', landing_views.landing_base, name='landingBase'),
    path('about', landing_views.about_us, name='aboutUs'),
    path('contact', landing_views.contact, name='contactUs'),
    #!SECTION 

    #SECTION Assistance URLs
	path('assistance/', assistance_views.assistanceHome, name='assistanceHome'),
    #!SECTION 

    #SECTION BADAC URLs
	path('badac/', badac_views.badacHome, name='badacHome'),
    #!SECTION 

    #SECTION BPSO URLs
	path('bpso/', bpso_views.bpsoHome, name='bpsoHome'),
    #!SECTION 

    #SECTION Katarungan URLs
    path('katarungan/', include('katarungan.urls')),
    #!SECTION

    #SECTION Residents URLs
    path('residents/', residents_views.residentsHome, name='residentsHome'),
    path('residents/add/', residents_views.residentsAdd, name='residentsAdd'),
    path('residents/view/', residents_views.residentsView, name='residentsView'),
    #!SECTION 

    #SECTION Senior & PWD URLs
    path('senior/', senior_views.seniorHome, name='seniorHome'),
    #!SECTION 

    #SECTION SK URLs
    path('sk/', sk_views.skHome, name='skHome'),
    #!SECTION 

    #SECTION User Account URLs
    path('user/profile', user_views.userProfile, name='userProfile'),
    path('user/profile/update', user_views.updateProfile, name='updateProfile'),
    #!SECTION 

    #SECTION VAWC & BCPC URLs
    path('vawc/', vawc_views.vawcHome, name='vawcHome'),
    #!SECTION 
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)