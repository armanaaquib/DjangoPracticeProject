from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

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

@method_decorator(login_required, name='dispatch')
class SchoolCreateView(CreateView):
  model = models.School
  fields = ['name', 'principal', 'location']
  template_name = 'school_form.html'
  success_url = reverse_lazy('school:schools')

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class SchoolUpdateView(UpdateView):
  model = models.School
  fields = ['name', 'principal']
  template_name = 'school_form.html'

@method_decorator(login_required, name='dispatch')
class SchoolDeleteView(DeleteView):
  context_object_name = 'school'
  model = models.School
  template_name = 'school_confirm_delete.html'
  success_url = reverse_lazy('school:schools')