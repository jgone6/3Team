from django.contrib.auth.models import User
from django.db import models

# Create your models here.

from Video.models import Video


class Comment(models.Model):
    member_id = models.ForeignKey(User, on_delete=models.CASCADE)
    video_id = models.ForeignKey(Video, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    create_date = models.DateTimeField(auto_now_add=True)