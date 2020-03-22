from django.shortcuts import render
from users.models import Users

# Create your views here.
def index(request):
  return render(request,'index.html')

def users(request):
  users = Users.objects.all()
  return render(request, 'users/users.html', {'users':users})