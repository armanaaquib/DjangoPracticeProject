from django.urls import path
from . import views

app_name = 'school'

urlpatterns = [
  path('', views.SchoolListView.as_view(), name='schools'),
  path('<int:pk>/', views.SchoolDetailView.as_view(), name='school-detail'),
]