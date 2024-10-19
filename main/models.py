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

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, email, password, **extra_fields)

class Account(AbstractBaseUser, PermissionsMixin):
    photo = models.ImageField(upload_to="profile/", blank=True)
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phonenumber = PhoneNumberField(blank=True)
    gender = models.CharField(max_length=1,choices=GENDER, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    # Specify unique related names for groups and user_permissions
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='account_set',
        related_query_name='account',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='account_set',
        related_query_name='account',
    )

    def __str__(self):
       return self.username

class Blog(models.Model):
    id = models.CharField(primary_key=True, default=uuid.uuid4, editable=False, max_length=36)
    thumbnail = models.ImageField(upload_to="thumbnail/")
    title = models.CharField(max_length=255, null=False, unique=True)
    description = models.CharField(max_length=255, null=False, unique=True, blank=False)
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    content = models.TextField(unique=True, blank=False)
    upload_date = models.DateTimeField(auto_now_add=datetime.now(), editable=False)

    def __str__(self):
        return self.title
    
class Report(models.Model):
    nik = models.IntegerField(null=False, unique=False, blank=False, max_length=16)
    name = models.CharField(null=False, blank=False, max_length=255)
    email = models.EmailField(blank=False, null=False)
    phonenumber = PhoneNumberField(blank=False)
    title = models.CharField(blank=False, null=True,max_length=255)
    description = models.TextField(blank=False)
    status = models.CharField(choices=STATUS)
    date = models.DateTimeField(auto_now_add=True)

class Announcement(models.Model):
    id = models.CharField(primary_key=True, default=uuid.uuid4, editable=False, max_length=255)
    thumbnail = models.ImageField(upload_to="thumbnail/")
    title = models.CharField(max_length=255)
    description = models.CharField(blank=True, max_length=1000)
    content = models.TextField(blank=False)
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
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