from django.contrib import admin
from .models import bpso
# Register your models here.

class bpsoDetails(admin.ModelAdmin):
    list_display        = ( "case_no", "case_type", "complainant", "case_status"  )
    search_fields       = ()
    readonly_fields     = ()

    filter_horizontal   = ()
    list_filter         = ()
    fieldsets           = ()


admin.site.register(bpso, bpsoDetails)