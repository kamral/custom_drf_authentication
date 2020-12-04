from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from django.contrib.auth.models import User


class User(AbstractUser):
    age=models.PositiveIntegerField(null=True,blank=True)
    password1 =models.CharField(max_length=100)
    password2 =models.CharField(max_length=100)

