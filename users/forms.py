from django import forms
from django.contrib.auth.models import User
from . import models

class UserForm(forms.ModelForm):

  class Meta:
    model = models.UserInfo
    fields = '__all__'

class UserInfoForm(forms.ModelForm):
  password = forms.CharField(widget=forms.PasswordInput())
  
  class Meta:
    model = User
    fields = ('username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):

  class Meta:
    model = models.UserProfileInfo
    fields = ('portfolio_site', 'profile_pic')