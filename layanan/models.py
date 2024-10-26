from django.db import models
from datetime import datetime
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
STATUS = (
    ('Menunggu', "Sedang diproses"),
    ('Selesai', 'Selesai diproses')
)
    
class Report(models.Model):
    nik = models.IntegerField(null=False, unique=False, blank=False)
    name = models.CharField(null=False, blank=False, max_length=255)
    email = models.EmailField(blank=False, null=False)
    phonenumber = PhoneNumberField(blank=False)
    title = models.CharField(blank=False, null=True,max_length=255)
    description = models.TextField(blank=False)
    status = models.CharField(choices=STATUS, max_length=255)
    date = models.DateTimeField(auto_now_add=datetime.now())

    class Meta:
        verbose_name_plural = "Pengaduan"