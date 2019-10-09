from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account


class AccountDetail(UserAdmin):
    list_display        = ('username', 'email','first_name','middle_name','last_name', 'sector','last_login',)
    search_fields       = ('email','username',)
    readonly_fields     = ('date_joined', 'last_login')

    filter_horizontal   = ()
    list_filter         = ()
    fieldsets           = ((None,{'fields':('username', 'email', 'first_name','middle_name','last_name', 'sector')}),)
    
    


    
    


admin.site.register(Account, AccountDetail)

