from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

from shop.base import BaseModel



class User(models.Model):
    first_name = models.CharField(max_length=50, null=True)
    phone_number = models.CharField(max_length=13, null=True)
    email = models.CharField(max_length=50, null=True)


