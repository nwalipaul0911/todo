from time import time
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from datetime import date
from .models import Task
from .forms import TaskForm
# Create your views here.
def index(request):
  return render(request, 'todo/index.html')
def home(request):
  form = TaskForm(request.POST)
  re_dir = 'home'
  tasks = Task.objects.all().filter(task_date = date.today(), status = False)
  if request.method == 'POST':
    form = TaskForm(request.POST)
    if form.is_valid:
      instance = form.save(commit=False)
      instance.user = request.user
      instance.save()
      return redirect('todo-home')
  context = {
    'form': form,
    'tasks': tasks,
    're_dir': re_dir
  }
  return render(request, 'todo/home.html', context)

def all(request):
  form = TaskForm(request.POST)
  re_dir = 'all'
  tasks = Task.objects.all().order_by('task_date')
  if request.method == 'POST':
    form = TaskForm(request.POST)
    if form.is_valid:
      instance = form.save(commit=False)
      instance.user = request.user
      instance.save()
      return redirect('todo-home')
  context = {
    'form': form,
    'tasks': tasks,
    're_dir': re_dir
  }
  return render(request, 'todo/all.html', context)

def done(request, id, prev):
  task = get_object_or_404(Task, id=id)
  if task.status == True:
    task.status = False
    task.save()
  else:
    task.status = True
    task.save()
  return redirect(f'todo-{prev}')

def delete_task(request, id, prev):
  task = get_object_or_404(Task, id=id)
  task.delete()
  return redirect(f'todo-{prev}')