from django.urls import path
from django.contrib.auth import views as reset_view
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path("idm/", IndexDesaMembangun, name="idm"),
    path("informasi/data/", DataPage, name="data"),
    path('tentang/sejarah/', HistoryPage, name="sejarah"),
    path('tentang/struktur/', StructurePage, name="struktur"),
    path('tentang/visi-misi-desa/', VisimisiPage, name="visimisi"),
    path('berita/',NewsPage, name="berita"),
    path('berita/<uuid:news_id>', NewsDetailPage, name="details"),
    path('informasi/pengaduan', ReportPage, name="pengaduan"),
    path('informasi/pengumuman/', AnnouncementPage, name="pengumuman"),
    path('informasi/kegiatan/', ActivitiesPage, name="kegiatan"),
]