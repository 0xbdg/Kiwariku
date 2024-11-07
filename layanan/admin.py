from django.contrib import admin
from .models import *

# Register your models here.


class ReportAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False 
    
    readonly_fields = ["name", "title", "phonenumber", "description"]

admin.site.register(Report, ReportAdmin)
"""
admin.site.register(SuratKematian)
admin.site.register(SuratTidakMampu)
admin.site.register(SuratNikah)
admin.site.register(SuratUsaha)
admin.site.register(SuratPindah)
"""