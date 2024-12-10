from django.db import models
from datetime import datetime
from phonenumber_field.modelfields import PhoneNumberField
from protected_media.models import ProtectedFileField

# Create your models here.
STATUS = (
    ('Sedang Diproses', "Sedang diproses"),
    ('Selesai Diproses', 'Selesai diproses')
)

class Report(models.Model):
    name = models.CharField(null=False, blank=False, max_length=255)
    phonenumber = PhoneNumberField(blank=False)
    title = models.CharField(blank=False, null=True,max_length=255)
    description = models.TextField(blank=False)
    status = models.CharField(choices=STATUS, max_length=255)
    date = models.DateTimeField(auto_now_add=datetime.now())

    def __str__(self):
        return self.title

    class Meta:
        verbose_name="Pengaduan"
        verbose_name_plural = "Pengaduan Warga"

class SuratNikah(models.Model):
    keterangan = models.TextField(null=False, blank=False)
    telefon = PhoneNumberField(region="ID")
    fotokopi_kartu_keluarga = ProtectedFileField(upload_to="kartu_keluarga/")
    surat_pengantar_rt_rw = ProtectedFileField(upload_to="surat_pengantar/")

    class Meta:
        verbose_name_plural = "Surat Nikah"

class SuratKematian(models.Model):
    keterangan = models.TextField(null=False, blank=False)
    telefon = PhoneNumberField(region="ID")
    fotokopi_kartu_keluarga = ProtectedFileField(upload_to="kartu_keluarga/")
    surat_pengantar_rt_rw = ProtectedFileField(upload_to="surat_pengantar/")
    surat_rumahsakit = ProtectedFileField(upload_to="surat_rumahsakit/", null=True, blank=True)

    class Meta:
        verbose_name_plural = "Surat Kematian"

class SuratTidakMampu(models.Model):
    keterangan = models.TextField(null=False, blank=False)
    telefon = PhoneNumberField(region="ID")
    fotokopi_kartu_keluarga = ProtectedFileField(upload_to="kartu_keluarga/")
    surat_pengantar_rt_rw = ProtectedFileField(upload_to="surat_pengantar/")

    class Meta:
        verbose_name_plural = "Surat Keterangan Tidak Mampu"

class SuratUsaha(models.Model):
    keterangan = models.TextField(null=False, blank=False)
    telefon = PhoneNumberField(region="ID")
    fotokopi_kartu_keluarga = ProtectedFileField(upload_to="kartu_keluarga/")
    surat_pengantar_rt_rw = ProtectedFileField(upload_to="surat_pengantar/")

    class Meta:
        verbose_name_plural = "Surat Usaha"

class SuratPindah(models.Model):
    keterangan = models.TextField(null=False, blank=False)
    telefon = PhoneNumberField(region="ID")
    fotokopi_kartu_keluarga = ProtectedFileField(upload_to="kartu_keluarga/")
    surat_pengantar_rt_rw = ProtectedFileField(upload_to="surat_pengantar/")

    class Meta:
        verbose_name_plural = "Surat Pindah"
