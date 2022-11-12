from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .models import User
from .forms import UserForm

# Create your views here.
def user_login(request):
  if request.method == 'POST':
    email = request.POST['email']
    password = request.POST['password']
    user = authenticate(email=email, password=password)
    if user is not None and user.is_active:
      login(request, user)
      return redirect('todo-home')
    else :
      return redirect('user-register')
  return render(request, 'user/login.html')

def user_logout(request):
  logout(request)
  return redirect('user-login')

def user_register(request):
  form = UserForm(request.POST)
  if request.method == 'POST':
    form = UserForm(request.POST)
    if form.is_valid:
      form.save()
      return redirect('user-login')
    else:
      form = UserForm()
  context = {
    'form': form
  }
  return render(request, 'user/register.html', context)