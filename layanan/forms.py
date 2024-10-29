from django import forms
from django.forms.widgets import *
from django.contrib.auth.forms import *
from phonenumber_field.formfields import PhoneNumberField

from .models import *

class LoginForm(forms.Form):
  username = forms.CharField(widget=TextInput(attrs={'class':'w-full text-base px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:border-gray-600'}), required=True)
  password = forms.CharField(widget=PasswordInput(attrs={'class':'w-full text-base px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:border-gray-600'}), required=True)

class PengajuanForm(forms.ModelForm):
  jenis = forms.ChoiceField(choices=SURAT,label="Pilih Jenis Surat",widget=Select(attrs={'class':'bg-white border w-full border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block  p-2.5 dark:bg-g dark:border-gray-600 dark:placeholder-gray-400 dark:text-black dark:focus:ring-blue-500 dark:focus:border-blue-500'}))
  keterangan = forms.CharField(widget=Textarea(attrs={'class':'peer  h-40 min-h-[50px] w-full resize-none rounded-[7px] border border-blue-gray-200  border-gray-300  px-3 py-2.5 font-sans text-sm font-normal text-blue-gray-700 outline outline-0 transition-all placeholder-shown:border placeholder-shown:border-blue-gray-200 placeholder-shown:border-t-blue-gray-200 focus:border-2 focus:border-gray-900 focus:border-t-transparent focus:outline-0 disabled:resize-none disabled:border-0 disabled:bg-blue-gray-50'}))
  telefon = forms.CharField(required=True,widget=TextInput(attrs={"class":"bg-white border w-full border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block  p-2.5 dark:bg-g dark:border-gray-600 dark:placeholder-gray-400 dark:text-black dark:focus:ring-blue-500 dark:focus:border-blue-500", "type":"tel", "placeholder": "e.g. +62 812 3456 7890"}))
  fotokopi_kartukeluarga = forms.FileField(required=True,widget=FileInput(attrs={'class':'block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-white dark:border-gray-600 dark:placeholder-gray-400'}))
  surat_pengantar_rt_rw = forms.FileField(required=True, widget=FileInput(attrs={'class':'block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-white dark:border-gray-600 dark:placeholder-gray-400'}))
  class Meta:
    model = PengajuanSurat
    fields = ["jenis","keterangan", "telefon", "fotokopi_kartukeluarga", "surat_pengantar_rt_rw"]