from django.contrib import admin
from .models import Katarungan

<<<<<<< HEAD
class KatarunganDetails(admin.ModelAdmin):
    list_display        = ( "case_no", "case_type", "complainant", "case_status"  )
    search_fields       = ()
=======
class CaseDetails(admin.ModelAdmin):
    model = CaseRecord
    list_display = ['get_name', 'case_no', 'case_type', 'complainant', 'case_status']
# 'get_case_no', 'get_case_type', 'get_complainant', 'get_case_status'
    def get_name(self, obj):\
        return  ("%s %s %s %s" % (obj.resident_case.first_name, obj.resident_case.middle_name, obj.resident_case.last_name, obj.resident_case.suffix)).upper()
    get_name.short_description = 'Full Name'

    search_fields       =  ('get_name','case_type', 'complainant', 'case_status', 'case_no')
>>>>>>> 78286c588bff0a00c4598a0b18bcc318b72091d8
    readonly_fields     = ()

    filter_horizontal   = ()
    list_filter         = ()
    fieldsets           = ()


<<<<<<< HEAD
admin.site.register(Katarungan, KatarunganDetails)
=======
admin.site.register(CaseRecord, CaseDetails)
>>>>>>> 78286c588bff0a00c4598a0b18bcc318b72091d8
