from django.contrib import admin
from .models import *

# Register your models here.


class ReportAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False 
    
    readonly_fields = ["name", "title", "phonenumber", "description"]

class SuratPengajuanAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False 
    
    readonly_fields = ['keterangan', 'telefon','surat_pengantar_rt_rw', 'fotokopi_kartu_keluarga']

admin.site.register(Report, ReportAdmin)
admin.site.register(SuratKematian, SuratPengajuanAdmin)
admin.site.register(SuratTidakMampu, SuratPengajuanAdmin)
admin.site.register(SuratNikah, SuratPengajuanAdmin)
admin.site.register(SuratUsaha, SuratPengajuanAdmin)
admin.site.register(SuratPindah, SuratPengajuanAdmin)
