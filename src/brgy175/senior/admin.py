from django.contrib import admin
from senior.models import Senior,Resident
# Register your models here.
class SeniorDetail(admin.ModelAdmin):
    model = Senior
    def full_name(obj):
        return ("%s %s %s %s" % (obj.resident.first_name, obj.resident.middle_name, obj.resident.last_name, obj.resident.suffix)).upper()
    full_name.short_description = 'Full Name'

    def age(obj):
        return ("%s Years Old" % (obj.resident.age)).upper()
    age_short_description = "Age"

    def civil_status(obj):
        return ("%s" % (obj.resident.civil_status)).upper()
    civil_status_short_description = "Civil Status"

    def gender(obj):
        return ("%s" % (obj.resident.gender)).upper()
    gender_short_description = "Gender"

    def date_of_birth(obj):
        return ("%s" % (obj.resident.date_of_birth)).upper()
    date_of_birth_short_description = "Date of Birth"

    list_display        = ( "senior_id", full_name, age, date_of_birth, gender, civil_status, )
    search_fields       = ()
    readonly_fields     = ()

    filter_horizontal   = ()
    list_filter         = ()
    fieldsets           = ()


# Register your models here.
# admin.site.register(Resident)
admin.site.register(Senior, SeniorDetail)