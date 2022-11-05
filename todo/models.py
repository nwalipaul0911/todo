from django.utils import timezone
from django.db import models
from user.models import User

 

# Create your models here.

class Task(models.Model):
  task_choices = (
    ('Work', 'Work'),
    ('Travel', 'Travel'),
    ('School', 'School'),
    ('Health', 'Health'),
    ('Personal', 'Personal')
  )
  category = models.CharField(max_length=50, choices=task_choices, default='Work')
  details = models.TextField(max_length=2000)
  task_date = models.DateField()
  task_time = models.TimeField()
  status = models.BooleanField(default=False)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
