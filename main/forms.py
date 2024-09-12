from django import forms
from django.contrib.auth.forms import *
from django.forms.widgets import TextInput, EmailInput, PasswordInput, CheckboxInput, DateInput
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

class KTPForm(forms.ModelForm):
  nik = forms.CharField(required=True,validators=[RegexValidator(regex=r'^\d{16}$',message='NIK harus terdiri dari 16 digit angka.',code='invalid_nik')], widget=TextInput(attrs={'class':'rounded-md p-1 w-full md:w-10/12','maxlength':'16'}))
  full_name = forms.CharField(required=True, widget=TextInput(attrs={'class':'rounded-md p-1 w-full md:w-10/12'}))
  birth_date = forms.DateField(required=True, widget=DateInput(attrs={'type':'date'}))
  gender = forms.ChoiceField(required=True,choices=GENDER, widget=forms.Select(attrs={"class":'bg-white border border-gray-300 text-gray-900 text-sm rounded-lg block p-2.5'}))
  address = forms.CharField(required=True, widget=TextInput(attrs={'class':'rounded-md p-5 w-full md:w-10/12'}))
  surat_pengantar = forms.BooleanField(widget=CheckboxInput(attrs={'class':'w-4 h-4 border-gray-50'}))
  fotocopy_ktp = forms.BooleanField(widget=CheckboxInput(attrs={'class':'w-4 h-4 border-gray-50'}))
  fotocopy_kk = forms.BooleanField(widget=CheckboxInput(attrs={'class':'w-4 h-4 border-gray-50'}))

  class Meta:
     model = KTP
     fields = ['nik', 'full_name', 'birth_date', 'gender', 'address', 'surat_pengantar', 'fotocopy_ktp', 'fotocopy_kk']