from django.db import models

# Create your models here.
import Member
import Video


class Comment(models.Model):
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE)
    video_id = models.ForeignKey(Video, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=100)
