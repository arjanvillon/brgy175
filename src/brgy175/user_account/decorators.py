from functools import wraps
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User


def superadmin_badac_only(function):
     @wraps(function)
     def wrap(request, *args, **kwargs):
          profile = request.user
          if profile.sector == 'badac':
               return function(request, *args, **kwargs)
          elif profile.sector == 'superadmin':
               return function(request, *args, **kwargs)  
          else:
               return HttpResponseRedirect('/home')

     return wrap

def superadmin_bpso_only(function):
     @wraps(function)
     def wrap(request, *args, **kwargs):
          profile = request.user
          if profile.sector == 'bpso':
               return function(request, *args, **kwargs)
          elif profile.sector == 'superadmin':
               return function(request, *args, **kwargs)     
          else:
               return HttpResponseRedirect('/home')

     return wrap

def superadmin_katarungan_only(function):
     @wraps(function)
     def wrap(request, *args, **kwargs):
          profile = request.user
          if profile.sector == 'katarungan':
               return function(request, *args, **kwargs)
          elif profile.sector == 'superadmin':
               return function(request, *args, **kwargs)  
          else:
               return HttpResponseRedirect('/home')

     return wrap

def superadmin_resident_only(function):
     @wraps(function)
     def wrap(request, *args, **kwargs):
          profile = request.user
          if profile.sector == 'resident':
               return function(request, *args, **kwargs)
          elif profile.sector == 'superadmin':
               return function(request, *args, **kwargs)      
          else:
               return HttpResponseRedirect('/home')

     return wrap

def superadmin_senior_only(function):
     @wraps(function)
     def wrap(request, *args, **kwargs):
          profile = request.user
          if profile.sector == 'senior':
               return function(request, *args, **kwargs)
          elif profile.sector == 'superadmin':
               return function(request, *args, **kwargs)  
          else:
               return HttpResponseRedirect('/home')

     return wrap

def superadmin_vawc_only(function):
     @wraps(function)
     def wrap(request, *args, **kwargs):
          profile = request.user
          if profile.sector == 'vawc':
               return function(request, *args, **kwargs)
          elif profile.sector == 'superadmin':
               return function(request, *args, **kwargs)  
          else:
               return HttpResponseRedirect('/home')

     return wrap