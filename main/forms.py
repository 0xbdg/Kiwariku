from django import forms
from django.contrib.auth.forms import *
from django.forms.widgets import TextInput, EmailInput, PasswordInput, NumberInput, DateInput
from phonenumber_field.formfields import PhoneNumberField

from .models import *

class RegisterForm(UserCreationForm):
    username = forms.CharField(required=True,widget=TextInput(attrs={'class':'border w-full text-base px-2  focus:outline-none focus:ring-0 focus:border-gray-600 rounded-md'}))
    first_name = forms.CharField(required=True,widget=TextInput(attrs={'class':'border w-full text-base px-2  focus:outline-none focus:ring-0 focus:border-gray-600 rounded-md'}))
    last_name = forms.CharField(required=True,widget=TextInput(attrs={'class':'border w-full text-base px-2  focus:outline-none focus:ring-0 focus:border-gray-600 rounded-md'}))
    email = forms.EmailField(required=True,widget=EmailInput(attrs={'class':'border w-full text-base px-2  focus:outline-none focus:ring-0 focus:border-gray-600 rounded-md'}))
    password1 = forms.CharField(required=True,widget=PasswordInput(attrs={'class':'border w-full text-base px-2  focus:outline-none focus:ring-0 focus:border-gray-600 rounded-md'}))
    password2 = forms.CharField(required=True,widget=PasswordInput(attrs={'class':'border w-full text-base px-2  focus:outline-none focus:ring-0 focus:border-gray-600 rounded-md'}))

    class Meta:
        model = Account
        fields = ["username","first_name","last_name","email","password1", "password2"]

class LoginForm(AuthenticationForm):
  username = forms.CharField(widget=TextInput(attrs={'class':'w-full text-base px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:border-gray-600','placeholder':'Username'}), required=True)
  password = forms.CharField(widget=PasswordInput(attrs={'class':'w-full text-base px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:border-gray-600','placeholder':'Password'}), required=True)
  class Meta:
    model = Account
    fields = ["username","password"]

class ProfileForm(): pass

class KTPForm(): pass