from django import forms
from .models import Video



class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ('title', 'member_id' , 'tag' )