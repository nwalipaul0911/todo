from django import forms 
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserForm(UserCreationForm):
  first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'First Name','type':'text'}))
  last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Last Name','type':'text'}))
  username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username','type':'text'}))
  email= forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'E-mail','type':'email'}))
  password1= forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter password','type':'password'}))
  password2= forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Re-enter password','type':'password'}))
  class Meta:
    model = User
    fields = ('first_name', 'last_name', 'email','username' ,'password1','password2')