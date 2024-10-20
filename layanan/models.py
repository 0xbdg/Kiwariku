from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from datetime import datetime
from phonenumber_field.modelfields import PhoneNumberField

import uuid

# Create your models here.

GENDER = (
    ("M","Laki-Laki"),
    ("F", "Perempuan")
)

STATUS = (
    ('Menunggu', "Sedang diproses"),
    ('Selesai', 'Selesai diproses')
)
    
class Report(models.Model):
    nik = models.IntegerField(null=False, unique=False, blank=False)
    name = models.CharField(null=False, blank=False, max_length=255)
    email = models.EmailField(blank=False, null=False)
    phonenumber = PhoneNumberField(blank=False)
    title = models.CharField(blank=False, null=True,max_length=255)
    description = models.TextField(blank=False)
    status = models.CharField(choices=STATUS, max_length=255)
    date = models.DateTimeField(auto_now_add=True)

class KTP(models.Model):
    nik = models.CharField(max_length=16,unique=True,validators=[RegexValidator(regex=r'^\d{16}$',message='NIK harus terdiri dari 16 digit angka.',code='invalid_nik')])
    nama_lengkap = models.CharField(max_length=255)
    tanggal_lahir = models.DateField(blank=False)
    jenis_kelamin = models.CharField(max_length=20,choices=GENDER, blank=False)
    alamat = models.CharField(max_length=255, blank=False)
    surat_pengantar_rtrw = models.BooleanField(default=False)
    fotocopy_ktp = models.BooleanField(default=False)
    fotocopy_kk = models.BooleanField(default=False)

    def __str__(self):
        return self.nama_lengkap
    

class Domicile(models.Model):
    nik = models.CharField(max_length=16,unique=True,validators=[RegexValidator(regex=r'^\d{16}$',message='NIK harus terdiri dari 16 digit angka.',code='invalid_nik')])
    nama_lengkap = models.CharField(max_length=255)
    tanggal_lahir = models.DateField(blank=False)
    jenis_kelamin = models.CharField(max_length=20,choices=GENDER, blank=False)
    alamat = models.CharField(max_length=255, blank=False)
    alamat_domisili = models.CharField(max_length=255, blank=False)
    tanggal_mulai = models.DateField(blank=False)
    surat_pengantar_rtrw = models.BooleanField(default=False)
    fotokopi_ktp = models.BooleanField(default=False)
    bukti_kepemilikan = models.BooleanField(default=False)
    surat_keterangan_rtrw = models.BooleanField(default=False)
    surat_belum_nikah = models.BooleanField(default=False)
    surat_izin_orangtua = models.BooleanField(default=False)

    def __str__(self):
        return self.nama_lengkap

class Divorce_Paper(models.Model):
    nik_suami = models.CharField(max_length=16,unique=True,validators=[RegexValidator(regex=r'^\d{16}$',message='NIK harus terdiri dari 16 digit angka.',code='invalid_nik')])
    nama_lengkap_suami = models.CharField(max_length=255)
    tanggal_lahir_suami = models.DateField(blank=False)
    alamat_suami = models.CharField(max_length=255, blank=False)
    nik_istri = models.CharField(max_length=16,unique=True,validators=[RegexValidator(regex=r'^\d{16}$',message='NIK harus terdiri dari 16 digit angka.',code='invalid_nik')])
    nama_lengkap_istri = models.CharField(max_length=255)
    tanggal_lahir_istri = models.DateField(blank=False)
    alamat_istri = models.CharField(max_length=255, blank=False)
    tanggal_cerai = models.DateField(blank=False)
    tempat_cerai = models.CharField(max_length=255, blank=False)
    nomor_tanggal_akta_cerai = models.CharField(max_length=255, blank=False)
    surat_pengantar_rtrw = models.BooleanField(default=False)
    fotokopi_ktp = models.BooleanField(default=False)
    fotokopi_kk = models.BooleanField(default=False)
    akta_cerai = models.BooleanField(default=False)
    surat_keterangan_pengadilan = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nama_lengkap_suami} - {self.nama_lengkap_istri}"

class Marriage_Paper(models.Model):
    nik_pengantin_pria = models.CharField(max_length=16,unique=True,validators=[RegexValidator(regex=r'^\d{16}$',message='NIK harus terdiri dari 16 digit angka.',code='invalid_nik')])
    nama_lengkap_pengantin_pria = models.CharField(max_length=255)
    tanggal_lahir_pengantin_pria = models.DateField(blank=False)
    alamat_pengantin_pria = models.CharField(max_length=255, blank=False)
    nik_pengantin_wanita = models.CharField(max_length=16,unique=True,validators=[RegexValidator(regex=r'^\d{16}$',message='NIK harus terdiri dari 16 digit angka.',code='invalid_nik')])
    nama_lengkap_pengantin_wanita = models.CharField(max_length=255)
    tanggal_lahir_pengantin_wanita = models.DateField(blank=False)
    alamat_pengantin_wanita = models.CharField(max_length=255, blank=False)
    tanggal_pernikahan = models.DateField(blank=False)
    tempat_pernikahan = models.CharField(max_length=255, blank=False)
    nama_saksi_pernikahan = models.CharField(max_length=255, blank=False)
    surat_pengantar_rtrw = models.BooleanField(default=False)
    fotokopi_ktp = models.BooleanField(default=False)
    fotokopi_kk = models.BooleanField(default=False)
    akta_kelahiran = models.BooleanField(default=False)
    surat_keterangan_belum_nikah = models.BooleanField(default=False)
    surat_izin_orangtua = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nama_lengkap_pengantin_pria} - {self.nama_lengkap_pengantin_wanita}"