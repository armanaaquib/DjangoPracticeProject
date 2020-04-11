from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from . import models

# Create your views here.
@method_decorator(login_required, name='dispatch')
class SchoolListView(ListView):
  template_name = 'school_list.html'
  context_object_name = 'schools'
  model = models.School

  def get_queryset(self):
    context = models.School.objects.filter(user=self.request.user)
    return context

@method_decorator(login_required, name='dispatch')
class SchoolDetailView(DetailView):
  template_name = 'school_detail.html'
  model = models.School