from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.template import Template, Context
from django.views.generic.base import View, TemplateView

from . import models, forms

# Create your views here.
class IndexView(TemplateView):
  template_name = 'users/index.html'

@login_required
def user_logout(request):
  logout(request)
  return HttpResponseRedirect(reverse('users:user_login'))

@method_decorator(login_required, name='dispatch')
class UsersView(TemplateView):
  template_name = 'users/users.html'

  def get_context_data(self):
    context = super().get_context_data()
    context['users'] = models.UserInfo.objects.all()
    return context

@login_required
def addUser(request):

  if request.method == 'POST':
    userForm = forms.UserForm(request.POST)

    if userForm.is_valid:
      userForm.save()
      return HttpResponseRedirect('/users')

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
      template = Template('''
        {% extends 'users/base.html' %}
        {% block title %}Error in Login{% endblock %}
        {% block body %}
          <h1>INVALID LOGIN DETAILS SUPPLIED!</h1>
        {% endblock %}
      ''')
      
      context = Context()
      return HttpResponse(template.render(context=context))

  login_form = forms.LoginForm()
  return render(request, 'users/login.html', {'login_form': login_form})

class AuthorView(View):
  def get(self, request):
    template = Template(
      '''
      {% extends 'users/base.html' %}
      {% block title %}Author Name{% endblock %}
      {% block body %}
        <h1>Author Name: Aaquib Equbal</h1>
      {% endblock %}
      '''
    )

    context = Context()
    return HttpResponse(template.render(context=context))
