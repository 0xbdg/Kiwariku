from django import forms
from django.contrib.auth.forms import *
from django.forms.widgets import TextInput, EmailInput, PasswordInput, NumberInput, DateInput

from .models import *

class RegisterForm(UserCreationForm):
    username = forms.CharField(widget=TextInput())
    email = forms.EmailField(widget=EmailInput())
    password1 = forms.CharField(widget=PasswordInput())
    password2 = forms.CharField(widget=PasswordInput())
    birth = forms.DateField(widget=DateInput())
    nik = forms.IntegerField(widget=NumberInput())

    class Meta:
        pass