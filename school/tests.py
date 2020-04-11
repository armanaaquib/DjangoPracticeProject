from django.test import TestCase
from django.contrib.auth.models import User
from .models import School, Student

# Create your tests here.
class TestSchoolModel(TestCase):
  def test_get_absolute_url(self):
    school = School(pk='1')
    self.assertEqual(school.get_absolute_url(), '/schools/1/')

  def test_str(self):
    school = School(name='MANUU')
    self.assertEqual(school.__str__(), 'MANUU')
