from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='todo-index'),
    path('home/', home, name='todo-home'),
    path('all/', all, name='todo-all'),
    path('done/<int:id>/<str:prev>', done, name='todo-done'),
    path('delete/<int:id>/<str:prev>', delete_task, name='todo-delete')
]