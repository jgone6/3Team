from django.db import models

# Create your models here.

from Video.models import Video

class Tag(models.Model):
    title = models.CharField(max_length=10)
    videotag = models.ManyToManyField(Video, related_name='videotag')