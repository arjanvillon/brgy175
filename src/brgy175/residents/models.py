from django.db import models
from django.utils import timezone
from django.urls import reverse

class Resident(models.Model):
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    suffix = models.CharField(max_length=3)
    address = models.CharField(max_length=100)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    place_of_birth = models.CharField(max_length=30)
    age = models.PositiveIntegerField()
    weight = models.PositiveIntegerField(null=True)
    height = models.PositiveIntegerField(null=True)
    gender = models.CharField(max_length=6)
    civil_status = models.CharField(max_length=10)
    contact_number = models.CharField(max_length=11)
    nationality = models.CharField(max_length=15)
    email_address = models.EmailField(max_length=60, unique=True)
    religion = models.CharField(max_length=30)

    is_senior = models.CharField(max_length=10)
    senior_id = models.CharField(max_length=15, default='')
    created_date = models.DateTimeField(default=timezone.now)

    is_pwd = models.CharField(max_length=10, default='no')
    pwd_id = models.CharField(max_length=15, default='')
    disability = models.CharField(max_length=50, default='')

    is_fresh_grad = models.CharField(max_length=10, default='no')

    resident_profile = models.ImageField(default='default_profile.jpg', upload_to='resident_profile_pics')

    def get_absolute_url(self):
        return reverse('residents:resident_detail', kwargs={'pk': self.pk})
 
    def __str__(self):
        return ("%s %s %s %s" % (self.first_name, self.middle_name, self.last_name, self.suffix))
    # citizen_id = models.IntegerField()
    # pwd_no = models.IntegerField()
    # is_senior = models.BooleanField(default=False)
    # is_fresh_grad = models.BooleanField(default=False)
    # is_pwd = models.BooleanField(default=False)

# class SchoolCredentials(models.Model):
#     student = models.ForeignKey(Resident, on_delete=models.CASCADE)
#     school = models.CharField(max_length=100)
#     year_level = models.IntegerField()
#     course = models.CharField(max_length=100)
#     father_name = models.CharField(max_length=90)
#     father_age = models.IntegerField()
#     father_address = models.CharField(max_length=100)
#     father_salary = models.FloatField()
#     father_precint = models.CharField(max_length=15)
#     mother_name = models.CharField(max_length=90)
#     mother_age = models.IntegerField()
#     mother_address = models.CharField(max_length=100)
#     mother_salary = models.FloatField()
#     mother_precint = models.CharField(max_length=15)

# class CaseRecord(models.Model):
#     case_holder = models.ForeignKey(Resident, on_delete=models.CASCADE)
#     complainant = models.CharField(max_length=100)
#     case_type = models.CharField(max_length=50)
#     case_number = models.CharField(max_length=20)
#     case_remarks = models.CharField(max_length=20)
