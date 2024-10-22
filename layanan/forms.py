from django import forms
from django.forms.widgets import TextInput, PasswordInput
from django.contrib.auth.forms import *
from superuser.models import Account

class LoginForm(AuthenticationForm):
  username = forms.CharField(widget=TextInput(attrs={'class':'w-full text-base px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:border-gray-600'}), required=True)
  password = forms.CharField(widget=PasswordInput(attrs={'class':'w-full text-base px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:border-gray-600'}), required=True)
  class Meta:
    model = Account
    fields = ["username","password"]