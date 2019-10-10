from django.contrib import admin
from .models import badac
# Register your models here.

class badacDetails(admin.ModelAdmin):
    list_display        = ( "case_no", "case_type", "complainant", "case_status"  )
    search_fields       = ()
    readonly_fields     = ()

    filter_horizontal   = ()
    list_filter         = ()
    fieldsets           = ()


admin.site.register(badac, badacDetails)