from django.shortcuts import render
from . import models, forms

# Create your views here.
def index(request):
  return render(request,'users/index.html')

def users(request):
  users = models.UserInfo.objects.all()
  return render(request, 'users/users.html', {'users':users})

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