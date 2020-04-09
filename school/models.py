from django.db import models

# Create your models here.
class School(models.Model):
  name = models.CharField(max_length=265)
  principal = models.CharField(max_length=265)
  location = models.CharField(max_length=265)

  def __str__(self):
    return self.name

class Student(models.Model):
  name = models.CharField(max_length=265)
  age = models.PositiveIntegerField()
  school = models.ForeignKey(School, related_name='schools', on_delete=models.CASCADE)

  def __str__(self):
    return self.name