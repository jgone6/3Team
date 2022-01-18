from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Comment(models.Model):
    like = models.ManyToManyField(User, related_name='likes', blank=True)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    contents = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)