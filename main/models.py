from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from datetime import datetime
from phonenumber_field.modelfields import PhoneNumberField
from ckeditor.fields import RichTextField

import uuid

# Create your models here.

GENDER = (
    ("M","Laki-Laki"),
    ("F", "Perempuan")
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
    photo = models.ImageField(upload_to="profile")
    nik = models.CharField(max_length=16,unique=True,blank=True,validators=[RegexValidator(regex=r'^\d{16}$',message='NIK harus terdiri dari 16 digit angka.',code='invalid_nik')])
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phonenumber = PhoneNumberField(blank=True)
    gender = models.CharField(max_length=1,choices=GENDER, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    date_joined = models.DateTimeField(default=datetime.now)

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

    def clean(self):
        # Validasi tambahan jika diperlukan
        if not self.nik.isdigit():
            raise ValidationError('NIK harus terdiri dari angka saja.')
        super().clean()

    def __str__(self):
       return self.username

    class Meta:
        db_table = 'Account'

class New(models.Model):
    id = models.CharField(primary_key=True, default=uuid.uuid4, editable=False, max_length=36)
    thumbnail = models.ImageField(upload_to="thumbnail/")
    title = models.CharField(max_length=255, null=False, unique=True)
    content = RichTextField()
    upload_date = models.DateTimeField(auto_now_add=datetime.now(), editable=False)

    def __str__(self):
        return self.title

class KTP(models.Model):
    nik = models.CharField(max_length=16,unique=True,validators=[RegexValidator(regex=r'^\d{16}$',message='NIK harus terdiri dari 16 digit angka.',code='invalid_nik')])
    full_name = models.CharField(max_length=255)
    birth_date = models.DateField(blank=False)
    gender = models.CharField(max_length=20,choices=GENDER, blank=False)
    address = models.CharField(max_length=255, blank=False)
    surat_pengantar = models.BooleanField(default=False)
    fotocopy_ktp = models.BooleanField(default=False)
    fotocopy_kk = models.BooleanField(default=False)
    

class Domicile(models.Model): pass

class Divorce_Paper(models.Model): pass

class Marriage_Paper(models.Model): pass