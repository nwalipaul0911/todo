from django.db import models
from django.contrib.auth.models import AbstractUser
 

# Create your models here.
class User(AbstractUser):
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  username = models.CharField(max_length = 20)
  email = models.EmailField(unique = True)
  password1= models.CharField(max_length=15)
  password2= models.CharField(max_length=15)
  USERNAME_FIELD='email'
  REQUIRED_FIELDS=['first_name', 'last_name', 'username']
  def __str__(self):
    return self.first_name
