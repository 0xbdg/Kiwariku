from django.db import models
from datetime import datetime
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
STATUS = (
    ('Sedang Diproses', "Sedang diproses"),
    ('Selesai Diproses', 'Selesai diproses')
)

SURAT = (
    ("SKP","Surat Keterangan Pindah"),
    ("SKN","Surat Keterangan Menikah"),
    ("SKTM","Surat Keterangan Tidak Mampu"),
    ('SKU',"Surat Keterangan Usaha"),
    ('SKM',"Surat Keterangan Meninggal")
)
    
class Report(models.Model):
    name = models.CharField(null=False, blank=False, max_length=255)
    email = models.EmailField(blank=False, null=False)
    phonenumber = PhoneNumberField(blank=False)
    title = models.CharField(blank=False, null=True,max_length=255)
    description = models.TextField(blank=False)
    status = models.CharField(choices=STATUS, max_length=255)
    date = models.DateTimeField(auto_now_add=datetime.now())

    class Meta:
        verbose_name_plural = "Pengaduan"

class PengajuanSurat(models.Model):
    jenis = models.CharField(max_length=255,choices=SURAT)
    keterangan = models.TextField(null=False, blank=False)
    telefon = PhoneNumberField(region="ID")
    fotokopi_kartu_keluarga = models.FileField(upload_to="kartu_keluarga/")
    surat_pengantar_rt_rw = models.FileField(upload_to="surat_pengantar/")

    class Meta:
        verbose_name_plural = "Pengajuan Surat"
