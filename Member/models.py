from django.db import models

# Create your models here.
import Video


class Member(models.Model):
    nickname = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    comment = models.ManyToManyField(Video, related_name='Comment')