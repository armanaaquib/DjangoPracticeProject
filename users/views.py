from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from . import models, forms

# Create your views here.
def index(request):
  return render(request,'users/index.html')

@login_required
def user_logout(request):
  logout(request)
  return HttpResponseRedirect(reverse('users:user_login'))

@login_required
def users(request):
  users = models.UserInfo.objects.all()
  return render(request, 'users/users.html', {'users':users})

@login_required
def addUser(request):

  if request.method == 'POST':
    userForm = forms.UserForm(request.POST)

    if userForm.is_valid:
      userForm.save()
      return users(request)

  userForm = forms.UserForm()
  return render(request, 'users/addUser.html',{'form' : userForm})

def register(request):

  registered = False

  if request.method == 'POST':
    userInfoForm = forms.UserInfoForm(data=request.POST)
    userProfileInfoForm = forms.UserProfileInfoForm(data=request.POST)

    if userInfoForm.is_valid() and userProfileInfoForm.is_valid():
      user_info = userInfoForm.save()
      user_info.set_password(user_info.password)
      user_info.save()

      user_profile_info = userProfileInfoForm.save(commit=False)
      user_profile_info.user = user_info

      if 'profile_pic' in request.FILES:
        user_profile_info.profile_pic = request.FILES['profile_pic']

      user_profile_info.save()

      registered = True

    else:
      print(userInfoForm.errors, userProfileInfoForm.errors)

  else:
    userInfoForm = forms.UserInfoForm()
    userProfileInfoForm = forms.UserProfileInfoForm()

  registration_detail = {
    'user_form': userInfoForm, 
    'profile_form': userProfileInfoForm, 
    'registered': registered,
  }

  return render(request, 'users/registration.html', context=registration_detail)

def user_login(request):
  
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(username=username, password=password)

    if user:
      
      if user.is_active:
        login(request, user)

        return HttpResponseRedirect(reverse('index'))
      else:
        return HttpResponse('<h1>ACCOUNT NOT ACTIVE</h1>')

    else:
      return HttpResponse('<h1>INVALID LOGIN DETAILS SUPPLIED!</h1>')

  login_form = forms.LoginForm()
  return render(request, 'users/login.html', {'login_form': login_form})