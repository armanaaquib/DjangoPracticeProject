from django.conf.urls import url

from . import views

app_name = 'users'

urlpatterns = [
  url(r'^$', views.users, name='users'),
  url(r'^add/$', views.addUser, name='addUser'),
  url(r'^register/$', views.register, name='register'),
]