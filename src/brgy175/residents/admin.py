from django.contrib import admin
from .models import Resident

class ResidentDetail(admin.ModelAdmin):
    # firstName = "first_name"
    # middleName = "middle_name"
    # lastName = "last_name"
    # fullName = "%s %s $s" % (firstName, middleName, lastName)
    def full_name(obj):
        return ("%s %s %s %s" % (obj.first_name, obj.middle_name, obj.last_name, obj.suffix)).upper()
    full_name.short_description = 'Full Name'

    list_display        = ( full_name, )
    search_fields       =  ()
    # list_display        = ( full_name, "age", "address", "date_of_birth", "gender", "civil_status", "contact_number", "email_address" )
    # search_fields       = ( 'first_name', 'last_name', 'email_address' )
    readonly_fields     = ()

    filter_horizontal   = ()
    list_filter         = ()
    fieldsets           = ()


# Register your models here.
# admin.site.register(Resident)
admin.site.register(Resident, ResidentDetail)