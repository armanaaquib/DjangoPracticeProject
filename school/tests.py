from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import School, Student

# Create your tests here.
class TestSchoolModel(TestCase):
  def test_get_absolute_url(self):
    school = School(pk='1')
    self.assertEqual(school.get_absolute_url(), '/schools/1/')

  def test_str(self):
    school = School(name='MANUU')
    self.assertEqual(school.__str__(), 'MANUU')

class TestStudentModel(TestCase):
  def test_get_absolute_url(self):
    school = School(pk='1')
    student = Student(school=school)
    self.assertEqual(student.get_absolute_url(), '/schools/1/')

  def test_str(self):
    student = Student(name='John')
    self.assertEqual(student.__str__(), 'John')

class TestSchoolListView(TestCase):
  def setUp(self):
    test_user = User.objects.create_user(username='john', password='jo-kl')
    test_user.save()

    no_of_schools = 10
    for school_id in range(no_of_schools):
      name = f'name-{school_id}'
      principal = f'principal-{school_id}'
      location = f'location-{school_id}'

      test_school = School.objects.create(
        name=name, 
        principal=principal, 
        location=location, 
        user=test_user
      )
      test_school.save()

  def test_redirect_if_not_logged_in(self):
    response = self.client.get(reverse('school:schools'))

    self.assertEqual(response.status_code, 302)
    self.assertTrue(response.url.startswith('/user_login'))

  def test_correct_user(self):
    self.client.login(username='john', password='jo-kl')
    response = self.client.get(reverse('school:schools'))

    self.assertEqual(response.status_code, 200)
    self.assertEqual(str(response.context['user']), 'john')

  def test_correct_context(self):
    self.client.login(username='john', password='jo-kl')
    response = self.client.get(reverse('school:schools'))

    self.assertEqual(len(response.context['schools']), 10)

  def test_uses_correct_template(self):
    self.client.login(username='john', password='jo-kl')
    response = self.client.get(reverse('school:schools'))

    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'school_list.html')