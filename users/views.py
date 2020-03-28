from django.shortcuts import render
from . import models, forms

# Create your views here.
def index(request):
  return render(request,'users/index.html')

def users(request):
  users = models.User.objects.all()
  return render(request, 'users/users.html', {'users':users})

def addUser(request):

  if request.method == 'POST':
    userForm = forms.UserForm(request.POST)

    if userForm.is_valid:
      userForm.save()
      return users(request)

  userForm = forms.UserForm()
  return render(request, 'users/addUser.html',{'form' : userForm})