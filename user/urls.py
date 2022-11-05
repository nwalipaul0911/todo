from django.urls import path
from .views import *

urlpatterns = [
  path('login/', user_login, name='user-login'),
  path('logout/', user_logout, name='user-logout'),
  path('register/', user_register, name='user-register'),
]