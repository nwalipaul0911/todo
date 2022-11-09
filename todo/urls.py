from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='todo-index'),
    path('home/', home, name='todo-home'),
    path('all/', all, name='todo-all'),
    path('api/<int:id>', api)
]