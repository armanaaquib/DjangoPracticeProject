from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class School(models.Model):
  name = models.CharField(max_length=265)
  principal = models.CharField(max_length=265)
  location = models.CharField(max_length=265)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def get_absolute_url(self):
    return reverse('school:detail', kwargs={'pk': self.pk})

  def __str__(self):
    return self.name

class Student(models.Model):
  name = models.CharField(max_length=265)
  age = models.PositiveIntegerField()
  school = models.ForeignKey(School, related_name='students', on_delete=models.CASCADE)

  def get_absolute_url(self):
    return reverse('school:detail', kwargs={'pk': self.school.pk})

  def __str__(self):
    return self.name