from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('login/', SignInView.as_view(), name="signin"),
    path('register/', RegisterView.as_view(), name="signup"),
    path('sejarah/', HistoryPage, name="sejarah"),
    path('struktur/', StructurePage, name="struktur"),
    path('berita/',NewsPage, name="berita"),
    path('account/profile', ProfilePage, name="profil"),
    path('layanan/ktp/', LayananKtpPage, name="ktp"),
    path('layanan/domisili/', LayananDomisiliPage, name="domisili"),
    path('layanan/surat_cerai/', LayananSuratCeraiPage, name="cerai"),
    path('layanan/surat_nikah/', LayananSuratNikahPage, name="nikah"),
]