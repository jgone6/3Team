from django import forms
from .models import Video
# from .models import UploadFileModel

# class UploadFileForm(forms.ModelForm):
#     class Meta:
#         model = UploadFileModel
#         fields = ('title', 'file', 'tag', 'like')
#
#     def __init__(self, *args, **kwargs):
#         super(PostForm, self).__init__(*args, **kwargs)
#         self.fields['file'].required = False


#
#
# class VideoForm(forms.ModelForm):
#     class Meta:
#         model = Video
#         fields = ('title', 'member_id' , 'tag' )


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        # fields = ('title', 'member_id', 'tag', 'like', 'file')
        fields = ('title', 'tag', 'file','file2')