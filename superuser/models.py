from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from datetime import datetime

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
    
class Announcement(models.Model):
    id = models.CharField(primary_key=True, default=uuid.uuid4, editable=False, max_length=255)
    thumbnail = models.ImageField(upload_to="thumbnail/")
    title = models.CharField(max_length=255)
    description = models.CharField(blank=True, max_length=1000)
    content = models.TextField(blank=False)
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Activities(models.Model):
    id = models.CharField(primary_key=True)
    thumbnail = models.ImageField(upload_to="thumbnail/")
    title = models.CharField(max_length=255)
    description = models.TextField(blank=False)
    location = models.CharField(blank=False)
    activity_date = models.DateField()
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title