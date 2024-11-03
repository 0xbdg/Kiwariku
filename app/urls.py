from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path("idm/", IndexDesaMembangun, name="idm"),
    path('tentang/sejarah/', HistoryPage, name="sejarah"),
    path('tentang/visi-misi-desa/', VisimisiPage, name="visimisi"),
    path('berita/artikel',NewsPage, name="berita"),
    path('berita/kegiatan/', ActivitiesPage, name="kegiatan"),
    path('berita/galeri/', GalleryPage, name="galeri"),
    path('berita/artikel/<uuid:news_id>', NewsDetailPage, name="details"),
    path('informasi/pengaduan', ReportPage, name="pengaduan"),
    path('informasi/pemerintah-desa', PemerintahdesaPage, name="pemerintah"),
    path('informasi/pengumuman/', AnnouncementPage, name="pengumuman"),
    path('data/pendidikan/', DataPendidikanPage, name="pendidikan"),
    path('data/pekerjaan/', DataPekerjaanPage, name="pekerjaan"),
    path('data/agama/', DataAgamaPage, name="agama")
]