from django.contrib import admin
from katarungan.models import Katarungan

# class KatarunganDetails(admin.ModelAdmin):
#     model = Katarungan
#     list_display = ['get_name', 'case_no', 'case_type', 'complainant', 'case_status']
# # 'get_case_no', 'get_case_type', 'get_complainant', 'get_case_status'
#     def get_name(self, obj):\
#         return  ("%s %s %s %s" % (obj.c_resident.first_name, obj.c_resident.middle_name, obj.c_resident.last_name, obj.c_resident.suffix)).upper()
#     get_name.short_description = 'Full Name'

#     search_fields       =  ('get_name','case_type', 'complainant', 'case_status', 'case_no')
#     readonly_fields     = ()

#     filter_horizontal   = ()
#     list_filter         = ()
#     fieldsets           = ()


admin.site.register(Katarungan)
