from django.urls import path
from .views import *

urlpatterns = [
    path("desa/kegiatan/",Kegiatan),
    path("desa/pengumuman/",Pengumuman),
    path("desa/galeri/", Galeri),
    path("desa/layanan/pengajuan/surat-kematian", SuratKematianUploadView.as_view()),
    path("desa/layanan/pengajuan/surat-nikah", SuratNikahUploadView.as_view()),
    path("desa/layanan/pengajuan/surat-usaha", SuratUsahaUploadView.as_view()),
    path("desa/layanan/pengajuan/surat-tidak-mampu", SuratTidakMampuUploadView.as_view()),
    path("desa/layanan/pengajuan/surat-pindah", SuratPindahUploadView.as_view()),
]
