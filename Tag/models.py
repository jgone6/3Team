from django.db import models

# Create your models here.
from Video.models import Video


class Tag(models.Model):
    title = models.CharField(max_length=10)
    video_has_tag = models.ManyToManyField(Video, related_name='tag')