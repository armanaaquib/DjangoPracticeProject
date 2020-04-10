from django.shortcuts import render
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from . import models

# Create your views here.
@method_decorator(login_required, name='dispatch')
class SchoolListView(ListView):
  context_object_name = 'schools'
  model = models.School