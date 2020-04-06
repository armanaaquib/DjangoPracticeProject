from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from . import models

class UserForm(forms.ModelForm):

  class Meta:
    model = models.UserInfo
    fields = '__all__'

class UserInfoForm(forms.ModelForm):
  password = forms.CharField(widget=forms.PasswordInput(), validators=[validate_password])
  confirm_password = forms.CharField(widget=forms.PasswordInput())
  
  class Meta:
    model = User
    fields = ('username', 'email', 'password', 'confirm_password')
  
  def clean(self):
    cleaned_data = super().clean()
    password = cleaned_data.get('password')
    confirm_password = cleaned_data.get('confirm_password')

    if password != confirm_password:
      raise forms.ValidationError('Passwords are not equal.')

class UserProfileInfoForm(forms.ModelForm):
  class Meta:
    model = models.UserProfileInfo
    fields = ('portfolio_site', 'profile_pic')

class LoginForm(forms.Form):
  username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'john@123'}))
  password = forms.CharField(widget=forms.PasswordInput())
