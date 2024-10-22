from django.urls import path
from django.contrib.auth import views as reset_view
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path("idm/", IndexDesaMembangun, name="idm"),
    path('sejarah/', HistoryPage, name="sejarah"),
    path('struktur/', StructurePage, name="struktur"),
    path('berita/',NewsPage, name="berita"),
    path('berita/<uuid:news_id>', NewsDetailPage, name="details"),
    path('informasi/pengaduan', ReportPage, name="pengaduan"),
    path('informasi/pengumuman/', AnnouncementPage, name="pengumuman"),
    path('informasi/kegiatan/', ActivitiesPage, name="kegiatan"),
]