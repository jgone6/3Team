from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# from Member.models import Member


class Video(models.Model):
    title = models.CharField(max_length=45)
    # tag_choices = (('mu','mu'),('va','va'),('do','do')('in','im'))
    tag = models.CharField(max_length=10)
    file = models.FileField(null=True)
    file2 = models.FileField(null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    # writer = models.ForeignKey(User, on_delete=models.CASCADE)

# class UploadFileModel(models.Model):
#     title = models.TextField(default='')
#     file = models.FileField(null=True)