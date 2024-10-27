from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from superuser.models import *

# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = Account
    list_display = ['username', 'is_staff', 'is_superuser']
    fieldsets = (
        ('Account', {'fields': ('email', 'username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ( 'is_staff', 'is_superuser','is_active')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'first_name', 'last_name','is_staff', 'is_superuser')}
        ),
    )
    search_fields = ('email', 'username', 'first_name', 'last_name')
    ordering = ('email',)

class CustomCitizen(admin.ModelAdmin):
    list_display = ["nama_lengkap","akun_layanan","NIK", "jenis_kelamin", "agama", "pekerjaan"]

    fieldsets = (
        ('Data penting', {'fields': ('NIK', 'KK')}),
        ('Informasi diri', {'fields': ('nama_lengkap', 'tempat_lahir', 'RT','RW','tanggal_lahir','alamat', 'jenis_kelamin', 'agama', 'pendidikan','pekerjaan')}),
        ('Layanan Mandiri', {'fields': ('akun_layanan',)})
    )

    list_filter = ('agama', 'pekerjaan', 'pendidikan', 'jenis_kelamin')

    search_fields = ("NIK","nama_lengkap")

admin.site.unregister(Group)
admin.site.register(Account, CustomUserAdmin)
admin.site.register(Blog)
admin.site.register(Announcement)
admin.site.register(Activity)
admin.site.register(Goverment)
admin.site.register(Citizen, CustomCitizen)