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
from user_account import views as user_account_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='user_account/login.html'), name='login' ),
    #path('register/', user_account_views.register, name='register'),
	path('katarungan/', include('katarungan.urls')),
	path('vawc/', include('vawc.urls')),
	path('badac/', include('badac.urls')),
	path('bpso/', include('bpso.urls')),
	path('senior/', include('senior.urls')),
	path('sk/', include('sk.urls')),
	path('assistance/', include('assistance.urls')),
	path('residents/', include('residents.urls')),
]


if settings.DEBUG:
    urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)