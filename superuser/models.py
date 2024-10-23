from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from datetime import datetime
from django_ckeditor_5.fields import CKEditor5Field
import uuid
# Create your models here.

GENDER = (
    ("M","Pria"),
    ("F", "Wanita")
)

RELIGION = (
    ("BUDDHA", "Buddha"),
    ("KRISTEN", "Kristen"),
    ("ISLAM", "Islam"),
    ("KATOLIK", "Katolik"),
    ("HINDU", "Hindu")
)

EDUCATION = (
    ("TK","TK/Kelompok Bermain"),
    ("SD","SD/Sederajat"),
    ("SMP", "SMP/Sederajat"),
    ("SMA", "SMA/Sederajat"),
    ("SMK", "SMK/Sederajat"),
    ("SLTP", "SLTP/Sederajat"),
    ("SLTA", "SLTA/Sederajat"),
    ("D1", "D-1/Sederajat"),
    ("D2", "D-2/Sederajat"),
    ("D3", "D-3/Sederajat"),
    ("D4", "D-4/Sederajat"),
    ("S1", "S-1/Sederajat"),
    ("S2", "S-2/Sederajat"),
)

JOB = (
    ("Penganggur", "Pengangguran"),
    ("Karyawan", "Karyawan")
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
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(default=datetime.now())

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
    content = CKEditor5Field("Content", config_name="extends")
    upload_date = models.DateTimeField(auto_now_add=datetime.now(), editable=False)

    def __str__(self):
        return self.title
    
class Announcement(models.Model):
    id = models.CharField(primary_key=True, default=uuid.uuid4, editable=False, max_length=255)
    thumbnail = models.ImageField(upload_to="thumbnail/")
    title = models.CharField(max_length=255)
    description = models.CharField(blank=True, max_length=1000)
    content = models.TextField(blank=False)
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=datetime.now())

    def __str__(self):
        return self.title

class Activity(models.Model):
    id = models.CharField(primary_key=True, default=uuid.uuid4, editable=False, max_length=36)
    thumbnail = models.ImageField(upload_to="thumbnail/")
    title = models.CharField(max_length=255)
    description = models.TextField(blank=False)
    location = models.CharField(blank=False, max_length=255)
    activity_date = models.DateField()
    upload_date = models.DateTimeField(auto_now_add=datetime.now())

    def __str__(self):
        return self.title
    
class Citizen(models.Model):
    NIK = models.CharField(max_length=16, null=False, blank=False, unique=True)
    KK = models.CharField(max_length=16, null=False, blank=False, unique=True)
    akun_layanan = models.OneToOneField(Account, on_delete=models.CASCADE, null=True, blank=True)
    nama_lengkap = models.CharField(max_length=255, null=False, blank=False)
    tempat_lahir = models.CharField(max_length=255, null=False, blank=False)
    RT = models.IntegerField(null=False, blank=False)
    RW = models.IntegerField(null=False, blank=False)
    tanggal_lahir = models.DateField(null=False, blank=False)
    alamat = models.CharField(max_length=500, null=False, blank=False)
    agama = models.CharField(max_length=255,choices=RELIGION, null=False, blank=False)
    jenis_kelamin = models.CharField(max_length=255, choices=GENDER, null=False,blank=False)
    pendidikan = models.CharField(max_length=255,choices=EDUCATION, null=False, blank=False)
    pekerjaan = models.CharField(max_length=255,choices=JOB, null=False, blank=False)

    def __str__(self):
        return self.nama_lengkap