from django import forms 
from .models import Task


class TaskForm(forms.ModelForm):
  task_choices = (
    ('Work', 'Work'),
    ('Travel', 'Travel'),
    ('School', 'School'),
    ('Health', 'Health'),
    ('Personal', 'Personal')
  )
  category = forms.CharField(widget=forms.Select(attrs={'placeholder':'Category'}, choices=task_choices))
  details = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Details'}))
  task_date = forms.DateField(widget=forms.DateInput(attrs={'name':'Date', 'type':'date'}))
  task_time = forms.TimeField(widget=forms.TimeInput(attrs={'name':'time', 'type':'time'}))
  class Meta:
    model = Task
    fields = ('category', 'details', 'task_date', 'task_time')
