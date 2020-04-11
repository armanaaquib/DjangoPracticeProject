from django.urls import path
from . import views

app_name = 'school'

urlpatterns = [
  path('', views.SchoolListView.as_view(), name='schools'),
  path('<int:pk>/', views.SchoolDetailView.as_view(), name='detail'),
  path('add/', views.SchoolCreateView.as_view(), name='add'),
  path('update/<int:pk>/', views.SchoolUpdateView.as_view(), name='update'),
  path('delete/<int:pk>/', views.SchoolDeleteView.as_view(), name='delete'),
  path('add_student/<int:school_id>/', views.StudentCreateView.as_view(), name='add-student'),
]