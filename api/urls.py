from django.urls import path
from .views import *

urlpatterns = [
    path("desa/kegiatan/",GetActivity),
    path("desa/pengumuman/",GetAnnouncement),
]
