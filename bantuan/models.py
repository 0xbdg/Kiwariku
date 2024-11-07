from django.db import models
from django.utils.html import format_html

# Create your models here.

SYARAT = (
    ("Memenuhi Syarat", "Memenuhi Syarat"),
    ("Tidak Memenuhi Syarat", "Tidak Memenuhi Syarat")
)

class BLT(models.Model):
    nama_penerima = models.CharField(max_length=500, null=False, blank=False)
    alamat = models.CharField(max_length=5000, null=False, blank=False)
    memenuhi_syarat =models.CharField(max_length=255,choices=SYARAT, null=False, blank=False)
    jumlah = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Rupiah")

    def rupiah(self):
        amount_str = f"{self.jumlah:,.0f}"
        return format_html("IDR {}", amount_str)
    
    def __str__(self):
        return self.nama_penerima
    
    class Meta:
        verbose_name="BLT"
        verbose_name_plural = "BLT"

class PKH(models.Model):
    nama = models.CharField(max_length=500, null=True, blank=True)
    alamat = models.CharField(max_length=5000, null=True, blank=True)
    rt = models.DecimalField(max_digits=3, decimal_places=0, verbose_name="RT", null=True, blank=True)

    def __str__(self):
        return self.nama_penerima

    class Meta:
        verbose_name="PKH"
        verbose_name_plural = "PKH"