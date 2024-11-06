from django import forms
from django.forms.widgets import *
from captcha.fields import CaptchaField
from phonenumber_field.formfields import PhoneNumberField

class ReportForm(forms.Form):
    name=forms.CharField(required=True, widget=TextInput(attrs={"class":"w-full p-2 border border-gray-600 rounded bg-transparent text-black min-h-[40px] outline-none"}))
    phonenumber=PhoneNumberField(region="ID")
    title=forms.CharField(required=True, widget=TextInput(attrs={"class":"w-full p-2 border border-gray-600 rounded bg-transparent text-black min-h-[40px] outline-none"}))
    description=forms.CharField(required=True, widget=Textarea(attrs={"class":"peer  h-40 min-h-[40px] w-full resize-none rounded-[7px] border border-blue-gray-200  border-gray-300  px-3 py-2.5 font-sans text-xs font-normal text-blue-gray-700 outline outline-0 transition-all placeholder-shown:border placeholder-shown:border-blue-gray-200 placeholder-shown:border-t-blue-gray-200 focus:border-2 focus:border-gray-900 focus:border-t-transparent focus:outline-0 disabled:resize-none disabled:border-0 disabled:bg-blue-gray-50"}))
    captcha = CaptchaField()