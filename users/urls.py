from django.conf.urls import url

from . import views

app_name = 'users'

urlpatterns = [
  url(r'^$', views.UsersView.as_view(), name='users'),
  url(r'^add/$', views.addUser, name='addUser'),
  url(r'^register/$', views.register, name='register'),
  url(r'^user_login/$', views.user_login, name='user_login'),
]