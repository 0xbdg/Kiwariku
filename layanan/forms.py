from django import forms
from django.contrib.auth.forms import *
from django.forms.widgets import TextInput, EmailInput, PasswordInput, CheckboxInput, DateInput
from phonenumber_field.formfields import PhoneNumberField

from superuser.models import *
from .models import *

class LoginForm(AuthenticationForm):
  username = forms.CharField(widget=TextInput(attrs={'class':'w-full text-base px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:border-gray-600'}), required=True)
  password = forms.CharField(widget=PasswordInput(attrs={'class':'w-full text-base px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:border-gray-600'}), required=True)
  class Meta:
    model = Account
    fields = ["username","password"]

class ProfileForm(forms.ModelForm):
  username = forms.CharField(required=True, widget=TextInput(attrs={'class':'input-field'}))
  first_name = forms.CharField(required=True, widget=TextInput(attrs={'class':'input-field'}))
  last_name = forms.CharField(required=True, widget=TextInput(attrs={'class':'input-field'}))
  birth_date = forms.DateField(required=False, widget=DateInput(attrs={'type':'date','class':'input-field'}))
  gender = forms.ChoiceField(required=True,choices=GENDER, widget=forms.Select(attrs={"class":'input-field'}))
  email = forms.EmailField(required=True,widget=EmailInput(attrs={'class':'input-field'}))
  phonenumber = PhoneNumberField()

  class Meta:
     model = Account
     fields = ['username', 'first_name', 'last_name', 'birth_date', 'gender', 'email', 'phonenumber']

class KTPForm(forms.ModelForm):
  nik = forms.CharField(required=True,validators=[RegexValidator(regex=r'^\d{16}$',message='NIK harus terdiri dari 16 digit angka.',code='invalid_nik')], widget=TextInput(attrs={'class':'rounded-md p-2 mb-4 w-full','maxlength':'16'}))
  nama_lengkap = forms.CharField(required=True, widget=TextInput(attrs={'class':'rounded-md p-2 mb-4 w-full'}))
  tanggal_lahir = forms.DateField(required=True, widget=DateInput(attrs={'type':'date','class':'rounded-md p-2 mb-4 w-full'}))
  jenis_kelamin = forms.ChoiceField(required=True,choices=GENDER, widget=forms.Select(attrs={"class":'bg-white border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block p-2.5 mb-4 w-full'}))
  alamat = forms.CharField(required=True, widget=TextInput(attrs={'class':'rounded-md p-2 mb-4 w-full'}))
  surat_pengantar_rtrw = forms.BooleanField(widget=CheckboxInput(attrs={'class':'w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500'}))
  fotocopy_ktp = forms.BooleanField(widget=CheckboxInput(attrs={'class':'w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500'}))
  fotocopy_kk = forms.BooleanField(widget=CheckboxInput(attrs={'class':'w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500'}))

  class Meta:
     model = KTP
     fields = ['nik', 'nama_lengkap', 'tanggal_lahir', 'jenis_kelamin', 'alamat', 'surat_pengantar_rtrw', 'fotocopy_ktp', 'fotocopy_kk']

class DomicileForm(forms.ModelForm):
  nik = forms.CharField(required=True,validators=[RegexValidator(regex=r'^\d{16}$',message='NIK harus terdiri dari 16 digit angka.',code='invalid_nik')], widget=TextInput(attrs={'class':'rounded-md p-2 mb-4 w-full','maxlength':'16'}))
  nama_lengkap = forms.CharField(required=True, widget=TextInput(attrs={'class':'rounded-md p-2 mb-4 w-full'}))
  tanggal_lahir = forms.DateField(required=True, widget=DateInput(attrs={'type':'date','class':'rounded-md p-2 mb-4 w-full'}))
  jenis_kelamin = forms.ChoiceField(required=True,choices=GENDER, widget=forms.Select(attrs={"class":'bg-white border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block p-2.5 mb-4 w-full'}))
  alamat = forms.CharField(required=True, widget=TextInput(attrs={'class':'rounded-md p-2 mb-4 w-full'}))
  alamat_domisili = forms.CharField(required=True, widget=TextInput(attrs={'class':'rounded-md p-2 mb-4 w-full'}))
  tanggal_mulai = forms.DateField(required=True, widget=DateInput(attrs={'type':'date','class':'rounded-md p-2 mb-4 w-full'}))
  surat_pengantar_rtrw = forms.BooleanField(required=True,widget=CheckboxInput(attrs={'class':'w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500'}))
  fotokopi_ktp = forms.BooleanField(required=True,widget=CheckboxInput(attrs={'class':'w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500'}))
  bukti_kepemilikan = forms.BooleanField(required=True,widget=CheckboxInput(attrs={'class':'w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500'}))
  surat_keterangan_rtrw = forms.BooleanField(required=False,widget=CheckboxInput(attrs={'class':'w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500'}))
  surat_belum_nikah = forms.BooleanField(required=False,widget=CheckboxInput(attrs={'class':'w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500'}))
  surat_izin_orangtua = forms.BooleanField(required=False,widget=CheckboxInput(attrs={'class':'w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500'}))

  class Meta:
     model = Domicile
     fields = ['nik', 'nama_lengkap', 'tanggal_lahir','jenis_kelamin', 'alamat', 'alamat_domisili', 'tanggal_mulai', 'surat_pengantar_rtrw', 'fotokopi_ktp','bukti_kepemilikan', 'surat_keterangan_rtrw', 'surat_belum_nikah', 'surat_izin_orangtua']

class DivorceForm(forms.ModelForm):
   nik_suami = forms.CharField(required=True,validators=[RegexValidator(regex=r'^\d{16}$',message='NIK harus terdiri dari 16 digit angka.',code='invalid_nik')], widget=TextInput(attrs={'class':'rounded-md p-2 mb-4 w-full','maxlength':'16'}))
   nama_lengkap_suami = forms.CharField(required=True, widget=TextInput(attrs={'class':'rounded-md p-2 mb-4 w-full'}))
   tanggal_lahir_suami = forms.DateField(required=True, widget=DateInput(attrs={'type':'date','class':'rounded-md p-2 mb-4 w-full'}))
   alamat_suami = forms.CharField(required=True, widget=TextInput(attrs={'class':'rounded-md p-2 mb-4 w-full'}))
   nik_istri = forms.CharField(required=True,validators=[RegexValidator(regex=r'^\d{16}$',message='NIK harus terdiri dari 16 digit angka.',code='invalid_nik')], widget=TextInput(attrs={'class':'rounded-md p-2 mb-4 w-full','maxlength':'16'}))
   nama_lengkap_istri = forms.CharField(required=True, widget=TextInput(attrs={'class':'rounded-md p-2 mb-4 w-full'}))
   tanggal_lahir_istri = forms.DateField(required=True, widget=DateInput(attrs={'type':'date','class':'rounded-md p-2 mb-4 w-full'}))
   alamat_istri = forms.CharField(required=True, widget=TextInput(attrs={'class':'rounded-md p-2 mb-4 w-full'}))
   tanggal_cerai = forms.DateField(required=True, widget=DateInput(attrs={'type':'date','class':'rounded-md p-2 mb-4 w-full'}))
   tempat_cerai = forms.CharField(required=True, widget=TextInput(attrs={'class':'rounded-md p-2 mb-4 w-full'}))
   nomor_tanggal_akta_cerai = forms.CharField(required=True, widget=TextInput(attrs={'class':'rounded-md p-2 mb-4 w-full'}))
   surat_pengantar_rtrw = forms.BooleanField(required=True,widget=CheckboxInput(attrs={'class':'w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500'}))
   fotokopi_ktp = forms.BooleanField(required=True,widget=CheckboxInput(attrs={'class':'w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500'}))
   fotokopi_kk = forms.BooleanField(required=True,widget=CheckboxInput(attrs={'class':'w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500'}))
   akta_cerai = forms.BooleanField(required=True,widget=CheckboxInput(attrs={'class':'w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500'}))
   surat_keterangan_pengadilan = forms.BooleanField(required=False,widget=CheckboxInput(attrs={'class':'w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500'}))

   class Meta:
      model = Divorce_Paper
      fields = ['nik_suami', 'nama_lengkap_suami', 'tanggal_lahir_suami', 'alamat_suami', 'nik_istri', 'nama_lengkap_istri', 'tanggal_lahir_istri', 'alamat_istri', 'tanggal_cerai', 'tempat_cerai', 'nomor_tanggal_akta_cerai', 'surat_pengantar_rtrw', 'fotokopi_ktp', 'fotokopi_kk', 'akta_cerai', 'surat_keterangan_pengadilan']

class MarriageForm(forms.ModelForm):
   nik_pengantin_pria = forms.CharField(required=True,validators=[RegexValidator(regex=r'^\d{16}$',message='NIK harus terdiri dari 16 digit angka.',code='invalid_nik')], widget=TextInput(attrs={'class':'rounded-md p-2 mb-4 w-full','maxlength':'16'}))
   nama_lengkap_pengantin_pria = forms.CharField(required=True, widget=TextInput(attrs={'class':'rounded-md p-2 mb-4 w-full'}))
   tanggal_lahir_pengantin_pria = forms.DateField(required=True, widget=DateInput(attrs={'type':'date','class':'rounded-md p-2 mb-4 w-full'}))
   alamat_pengantin_pria = forms.CharField(required=True, widget=TextInput(attrs={'class':'rounded-md p-2 mb-4 w-full'}))
   nik_pengantin_wanita = forms.CharField(required=True,validators=[RegexValidator(regex=r'^\d{16}$',message='NIK harus terdiri dari 16 digit angka.',code='invalid_nik')], widget=TextInput(attrs={'class':'rounded-md p-2 mb-4 w-full','maxlength':'16'}))
   nama_lengkap_pengantin_wanita = forms.CharField(required=True, widget=TextInput(attrs={'class':'rounded-md p-2 mb-4 w-full'}))
   tanggal_lahir_pengantin_wanita = forms.DateField(required=True, widget=DateInput(attrs={'type':'date','class':'rounded-md p-2 mb-4 w-full'}))
   alamat_pengantin_wanita = forms.CharField(required=True, widget=TextInput(attrs={'class':'rounded-md p-2 mb-4 w-full'}))
   tanggal_pernikahan = forms.DateField(required=True, widget=DateInput(attrs={'type':'date','class':'rounded-md p-2 mb-4 w-full'}))
   tempat_pernikahan = forms.CharField(required=True, widget=TextInput(attrs={'class':'rounded-md p-2 mb-4 w-full'}))
   nama_saksi_pernikahan = forms.CharField(required=True, widget=TextInput(attrs={'class':'rounded-md p-2 mb-4 w-full'}))
   surat_pengantar_rtrw = forms.BooleanField(required=True,widget=CheckboxInput(attrs={'class':'w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500'}))
   fotokopi_ktp = forms.BooleanField(required=True,widget=CheckboxInput(attrs={'class':'w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500'}))
   fotokopi_kk = forms.BooleanField(required=True,widget=CheckboxInput(attrs={'class':'w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500'}))
   akta_kelahiran = forms.BooleanField(required=True,widget=CheckboxInput(attrs={'class':'w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500'}))
   surat_keterangan_belum_nikah = forms.BooleanField(required=False,widget=CheckboxInput(attrs={'class':'w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500'}))
   surat_izin_orangtua = forms.BooleanField(required=False,widget=CheckboxInput(attrs={'class':'w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500'}))

   class Meta:
      model = Marriage_Paper
      fields = ['nik_pengantin_pria', 'nama_lengkap_pengantin_pria', 'tanggal_lahir_pengantin_pria', 'alamat_pengantin_pria', 'nik_pengantin_wanita', 'nama_lengkap_pengantin_wanita', 'tanggal_lahir_pengantin_wanita', 'alamat_pengantin_wanita', 'tanggal_pernikahan', 'tempat_pernikahan', 'nama_saksi_pernikahan', 'surat_pengantar_rtrw', 'fotokopi_ktp', 'fotokopi_kk', 'akta_kelahiran', 'surat_keterangan_belum_nikah', "surat_izin_orangtua"]