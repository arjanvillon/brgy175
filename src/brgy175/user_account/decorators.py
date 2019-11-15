from functools import wraps
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.mixins import AccessMixin



class superadmin_katarungan_only(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
          profile = request.user
          if not profile.sector == 'Katarungan' and not profile.sector == 'superadmin' :
               return self.handle_no_permission()   
          return super().dispatch(request, *args, **kwargs)

class superadmin_bpso_only(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
          profile = request.user
          if not profile.sector == 'bpso' and not profile.sector == 'superadmin' :
               return self.handle_no_permission()   
          return super().dispatch(request, *args, **kwargs)

class superadmin_vawc_only(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
          profile = request.user
          if not profile.sector == 'vawc' and not profile.sector == 'superadmin' :
               return self.handle_no_permission()   
          return super().dispatch(request, *args, **kwargs)


class superadmin_senior_only(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
          profile = request.user
          if not profile.sector == 'bpso' and not profile.sector == 'superadmin' :
               return self.handle_no_permission()   
          return super().dispatch(request, *args, **kwargs)

class superadmin_resident_only(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
          profile = request.user
          if not profile.sector == 'resident' and not profile.sector == 'superadmin' :
               return self.handle_no_permission()   
          return super().dispatch(request, *args, **kwargs)

class superadmin_bpso_only(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
          profile = request.user
          if not profile.sector == 'bpso' and not profile.sector == 'superadmin' :
               return self.handle_no_permission()   
          return super().dispatch(request, *args, **kwargs)

class superadmin_badac_only(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
          profile = request.user
          if not profile.sector == 'badac' and not profile.sector == 'superadmin' :
               return self.handle_no_permission()   
          return super().dispatch(request, *args, **kwargs)