from django.conf.urls import url
from . import views

app_name = 'school'

urlpatterns = [
  url(r'^$', views.SchoolListView.as_view(), name='schools'),
]