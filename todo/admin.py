from django.contrib import admin
from .models import Task

# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
  list_display=('id', 'details')
  list_display_links=  ('id', 'details')
  search_fields = ('id', 'details')
  list_filter= ('category', 'details')