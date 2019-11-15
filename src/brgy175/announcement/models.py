from django.db import models
from django.utils import timezone
from django.utils.deconstruct import deconstructible
from django.urls import reverse
import os
import datetime

from user_account.models import Account

# Create your models here.
class Announcement(models.Model):
    author = models.ForeignKey('user_account.Account', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    picture = models.ImageField(default='default.jpg', upload_to='announcement_pics')
    created_date = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse("announcement:announcement_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title








    




