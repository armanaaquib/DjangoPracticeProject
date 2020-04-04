import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','user_list.settings')

import django
django.setup()

from users.models import UserInfo

from faker import Faker
fakegen = Faker()

def populate(N=5):
  
  for entry in range(N):
    
    fake_first_name = fakegen.first_name()
    fake_last_name = fakegen.last_name()
    fake_email = fakegen.email()

    UserInfo.objects.create(first_name=fake_first_name,last_name=fake_last_name,email=fake_email)

if __name__ == '__main__':
  print('populating...')
  populate(20)