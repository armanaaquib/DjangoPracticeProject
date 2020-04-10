from django.conf.urls import url

from . import views

app_name = 'users'

urlpatterns = [
  url(r'^$', views.UsersView.as_view(), name='users'),
  url(r'^add/$', views.addUser, name='addUser'),
]