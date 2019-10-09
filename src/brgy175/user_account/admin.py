from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account


class AccountDetail(UserAdmin):
    list_display        = ( 'username','email', 'sector','first_name','middle_name','last_name',)
    search_fields       = ('email','username',)
    readonly_fields     = ('date_joined', 'last_login')

    filter_horizontal   = ()
    list_filter         = ()
    fieldsets           = ()

admin.site.register(Account, AccountDetail)