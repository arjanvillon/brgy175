from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


class MyAccountManager(BaseUserManager):
	def create_user(self, email, username,first_name, middle_name, last_name, sector, password=None,):
		if not email:
			raise ValueError('Users must have an email address')
		if not username:
			raise ValueError('Users must have a username')

		user = self.model(
            first_name =first_name,
            middle_name =middle_name,
            last_name =last_name,
            sector =sector,
			email=self.normalize_email(email),
			username=username,
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, username, first_name, middle_name, last_name, sector, password,):
		user = self.create_user(
            first_name =first_name,
            middle_name =middle_name,
            last_name =last_name,
            sector =sector,
            email=self.normalize_email(email),
			password=password,
			username=username,
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user





class Account(AbstractBaseUser):
    email               = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username            = models.CharField(max_length=30, unique=True,  )
    date_joined         = models.DateTimeField(verbose_name='date_joined', auto_now_add=True)
    last_login          = models.DateTimeField(verbose_name='last_login', auto_now=True)
    is_admin            = models.BooleanField(default=False)
    is_active           = models.BooleanField(default=True)
    is_staff            = models.BooleanField(default=False)
    is_superuser        = models.BooleanField(default=False)
    first_name          = models.CharField(max_length=30)
    middle_name         = models.CharField(max_length=30)
    last_name           = models.CharField(max_length=30)
    sector              = models.CharField(max_length=30)
    picture             = models.ImageField(default='default.jpg', upload_to='user_pics')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','first_name','middle_name','last_name','sector']

    objects = MyAccountManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
    
  

