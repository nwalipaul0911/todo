from time import time
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from datetime import date
from .models import Task
from .forms import TaskForm
from .serializers import TaskSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
# Create your views here.
def index(request):
  return render(request, 'todo/index.html')
def home(request):
  form = TaskForm(request.POST)
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
  }
  return render(request, 'todo/home.html', context)

def all(request):
  form = TaskForm(request.POST)
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
  }
  return render(request, 'todo/all.html', context)

@csrf_exempt
def api(request, id):
  task = get_object_or_404(Task, id=id)
  if request.method == 'GET':
    serializer = TaskSerializer(task)
    return JsonResponse(serializer.data)
  elif request.method =='PUT':
    data = JSONParser().parse(request)
    serializer = TaskSerializer(task, data=data)
    if serializer.is_valid():
      serializer.save()
      return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=400)
  elif request.method == 'DELETE':
    task.delete()
    return HttpResponse(status=204)
