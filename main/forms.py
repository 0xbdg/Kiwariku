from django import forms
from django.contrib.auth.forms import *
from django.forms.widgets import TextInput, EmailInput, PasswordInput, NumberInput, DateInput
from phonenumber_field.modelfields import PhoneNumberField

from .models import *

class RegisterForm(UserCreationForm):
    username = forms.CharField(widget=TextInput())
    birth = forms.DateField(widget=DateInput())
    email = forms.EmailField(widget=EmailInput())
    password1 = forms.CharField(widget=PasswordInput())
    password2 = forms.CharField(widget=PasswordInput())

    class Meta:
        pass

class LoginForm(AuthenticationForm):
  username = forms.CharField(widget=TextInput(attrs={'class':'border w-full text-base px-2 py-1 focus:outline-none focus:ring-0 focus:border-gray-600','placeholder':'Username'}))
  password = forms.CharField(widget=PasswordInput(attrs={'class':'border w-full text-base px-2 py-1 focus:outline-none focus:ring-0 focus:border-gray-600','id':'password','placeholder':'Password'}))
  class Meta:
    model = tbl_account
    fields = ["username","password"]