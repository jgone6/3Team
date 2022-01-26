from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    new_password = models.CharField(max_length=15, blank=True)
    email = models.EmailField(max_length=128, null=True)