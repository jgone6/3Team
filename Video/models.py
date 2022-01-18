from django.db import models

# Create your models here.
from Member.models import Member


class Video(models.Model):
    title = models.CharField(max_length=10)
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE)
    tag = models.CharField(max_length=10)
