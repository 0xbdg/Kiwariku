from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path("idm/", IndexDesaMembangun, name="idm"),
    path('tentang/sejarah/', HistoryPage, name="sejarah"),
    path('tentang/struktur/', StructurePage, name="struktur"),
    path('tentang/visi-misi-desa/', VisimisiPage, name="visimisi"),
    path('berita/',NewsPage, name="berita"),
    path('berita/<uuid:news_id>', NewsDetailPage, name="details"),
    path('informasi/pengaduan', ReportPage, name="pengaduan"),
    path('informasi/pemerintah-desa', PemerintahdesaPage, name="pemerintah"),
    path('informasi/pengumuman/', AnnouncementPage, name="pengumuman"),
    path('informasi/kegiatan/', ActivitiesPage, name="kegiatan"),
    path('data/pendidikan/', DataPendidikanPage, name="pendidikan"),
    path('data/pekerjaan/', DataPekerjaanPage, name="pekerjaan"),
    path('data/agama/', DataAgamaPage, name="agama")
]