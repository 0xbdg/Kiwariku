from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = tbl_account
    list_display = ['username', 'first_name', 'last_name','email','phonenumber', 'is_staff', 'is_active', 'date_joined']
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'phonenumber')}),
        ('Permissions', {'fields': ('is_active', 'is_staff')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'first_name', 'last_name', 'phonenumber', 'is_active', 'is_staff')}
        ),
    )
    search_fields = ('email', 'username', 'firstname', 'lastname', 'phonenumber')
    ordering = ('email',)

admin.site.register(tbl_account, CustomUserAdmin)