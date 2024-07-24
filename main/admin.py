from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import *

# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = tbl_account
    list_display = ['username', 'email','phonenumber','gender', 'is_staff', 'is_superuser', 'date_joined']
    fieldsets = (
        ('Account', {'fields': ('email', 'username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'phonenumber', 'gender', 'birth_date')}),
        ('Permissions', {'fields': ( 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'first_name', 'last_name', 'phonenumber', 'gender','birth_date','is_staff', 'is_superuser')}
        ),
    )
    search_fields = ('email', 'username', 'firstname', 'lastname', 'phonenumber', 'gender', 'birth_date')
    ordering = ('email',)

admin.site.unregister(Group)
admin.site.register(tbl_account, CustomUserAdmin)