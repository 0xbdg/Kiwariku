from django import forms
from django.contrib.auth.forms import *
from django.forms.widgets import TextInput, EmailInput, PasswordInput, NumberInput, DateInput
from phonenumber_field.formfields import PhoneNumberField

from .models import *

class RegisterForm(UserCreationForm):
    username = forms.CharField(widget=TextInput())
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(widget=EmailInput())
    phonenumber = PhoneNumberField(region="ID")
    password1 = forms.CharField(widget=PasswordInput())
    password2 = forms.CharField(widget=PasswordInput())

    class Meta:
        model = tbl_account
        fields = ["username","first_name","last_name","email","phonenumber", "password1", "password2"]

class LoginForm(AuthenticationForm):
  username = forms.CharField(widget=TextInput(attrs={'class':'border w-full text-base px-2 py-1 focus:outline-none focus:ring-0 focus:border-gray-600','placeholder':'Username'}), required=True)
  password = forms.CharField(widget=PasswordInput(attrs={'class':'border w-full text-base px-2 py-1 focus:outline-none focus:ring-0 focus:border-gray-600','placeholder':'Password'}), required=True)
  class Meta:
    model = tbl_account
    fields = ["username","password"]

class UpdateForm(): pass