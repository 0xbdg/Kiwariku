from django.db import models

# Create your models here.

class PKK(models.Model):
    nama_pengurus = models.CharField(max_length=255, null=False, blank=False)
    jabatan = models.CharField(max_length=255, null=False, blank=False)
    alamat = models.CharField(max_length=1000, null=False, blank=False)

    def __str__(self):
        return self.nama_pengurus

    class Meta:
        verbose_name="PKK"
        verbose_name_plural = "PKK"

class Posyandu(models.Model):
    nama = models.CharField(max_length=255, null=False, blank=False)
    nama_posyandu = models.CharField(max_length=255, null=True, blank=True)
    alamat = models.CharField(max_length=1000, null=False, blank=False)

    def __str__(self):
        return self.nama

    class Meta:
        verbose_name="Posyandu"
        verbose_name_plural = "Posyandu"

class BPD(models.Model):
    nama = models.CharField(max_length=255, null=False, blank=False)
    jabatan = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.nama

    class Meta:
        verbose_name="Pengurus"
        verbose_name_plural = "BPD"

class BUMDES(models.Model):
    nama_bumdes = models.CharField(max_length=255, null=False, blank=False)
    alamat_kantor = models.CharField(max_length=1000, null=False, blank=False)
    struktur = models.ImageField(upload_to="struktur_bumdes/")
    foto_bumdes = models.ImageField(upload_to="bumdes/")

    def __str__(self):
        return self.nama_bumdes

    class Meta:
        verbose_name="BUMdes"
        verbose_name_plural = "BUMdes"

class KarangTaruna(models.Model):
    nama = models.CharField(max_length=255, null=False, blank=False)
    jabatan = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.nama 

    class Meta:
        verbose_name="Pengurus"
        verbose_name_plural = "Karang Taruna"