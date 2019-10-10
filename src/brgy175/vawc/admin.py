from django.contrib import admin
from .models import vawc
# Register your models here.

class vawcDetails(admin.ModelAdmin):
    list_display        = ( "case_no", "case_type", "complainant", "case_status"  )
    search_fields       = ()
    readonly_fields     = ()

    filter_horizontal   = ()
    list_filter         = ()
    fieldsets           = ()


admin.site.register(vawc, vawcDetails)