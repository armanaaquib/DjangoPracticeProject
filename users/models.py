from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserInfo(models.Model):
  first_name = models.CharField(max_length=264)
  last_name = models.CharField(max_length=264)
  email = models.EmailField(unique=True)

  def __str__(self):
    return f'name: {self.first_name + self.last_name}\nEmail: {self.email}'

class UserProfileInfo(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)

  portfolio_site = models.URLField(blank=False)
  profile_pic = models.ImageField(upload_to='profile_pics', blank=False)

  def __str__(self):
    return self.user.username