from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = Account
    list_display = ['username', 'email','is_staff', 'is_superuser']
    fieldsets = (
        ('Account', {'fields': ('email', 'username', 'password')}),
        ('Personal Info', {'fields': ("photo",'first_name', 'last_name', 'phonenumber', 'gender', 'birth_date')}),
        ('Permissions', {'fields': ( 'is_staff', 'is_superuser','is_active')}),
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