from django.urls import path
from .views import *

urlpatterns = [
    path("desa/kegiatan/",Kegiatan),
    path("desa/pengumuman/",Pengumuman),
    path("desa/galeri/", Galeri)
]
