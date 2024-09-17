from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('account/login/', SignInView.as_view(), name="signin"),
    path('account/register/', RegisterView.as_view(), name="signup"),
    path('account/logout/', logout, name="signout"),
    path('account/profile', ProfilePage, name="profile"),
    path('account/profile/change_password', ChangePasswordPage, name="change"),
    path('sejarah/', HistoryPage, name="sejarah"),
    path('struktur/', StructurePage, name="struktur"),
    path('berita/',NewsPage, name="berita"),
    path('berita/<uuid:news_id>', NewsDetailPage, name="details"),
    path('layanan/ktp/', LayananKtpPage, name="ktp"),
    path('layanan/domisili/', LayananDomisiliPage, name="domisili"),
    path('layanan/surat_cerai/', LayananSuratCeraiPage, name="cerai"),
    path('layanan/surat_nikah/', LayananSuratNikahPage, name="nikah"),
]