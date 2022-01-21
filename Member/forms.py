from django import forms
from .models import Member
from django.contrib.auth.forms import PasswordChangeForm

class MemberForm(forms.ModelForm) :
    class Meta :
        model = Member
        fields = ('nickname', 'phone', 'new_password')
