# Generated by Django 3.2 on 2022-11-04 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_task_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='title',
        ),
    ]
