from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path("idm/", IndexDesaMembangun, name="idm"),
    path('tentang/sejarah/', HistoryPage, name="sejarah"),
    path('tentang/visi-misi-desa/', VisimisiPage, name="visimisi"),
    path('berita/artikel',NewsPage, name="berita"),
    path('berita/kegiatan/', ActivitiesPage, name="kegiatan"),
    path('informasi/galeri/', GalleryPage, name="galeri"),
    path('berita/artikel/<uuid:news_id>', NewsDetailPage, name="details"),
    path('informasi/pengaduan', ReportPage, name="pengaduan"),
    path('informasi/pemerintah-desa', PemerintahdesaPage, name="pemerintah"),
    path('informasi/pengumuman/', AnnouncementPage, name="pengumuman"),
    path('data/pendidikan/', DataPendidikanPage, name="pendidikan"),
    path('data/pekerjaan/', DataPekerjaanPage, name="pekerjaan"),
    path('data/agama/', DataAgamaPage, name="agama"),
    path('bantuan/blt/', BantuanBLT, name="blt"),
    path('bantuan/pkh/', BantuanPKH, name="pkh"),
    path('bantuan/bpnt/', BantuanBPNT, name="bpnt"),
    path('bantuan/stunting/', BantuanStunting, name="stunting"),
    path('bantuan/bpjs/', BantuanBPJS, name="bpjs"),
    path('bantuan/bansos/', BantuanBansos, name="bansos"),
    path('lembaga/pkk', PKK, name="PKK"),
    path('lembaga/posyandu', Posyandu, name="posyandu"),
]