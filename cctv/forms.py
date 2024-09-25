from django import forms
from django.forms.widgets import TextInput, PasswordInput
class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, widget=TextInput(attrs={'class':'border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}))
    password = forms.CharField(widget=PasswordInput(attrs={'class':'border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}))