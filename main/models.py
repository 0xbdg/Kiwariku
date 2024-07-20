from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.

GENDER = (
    ("Laki-Laki","Laki-Laki"),
    ("Perempuan", "Perempuan")
)

class CustomUsers(AbstractBaseUser):
    pass

class tbl_admin(CustomUsers):
    pass

class tbl_user(CustomUsers):
    pass