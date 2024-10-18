from django.urls import path
from django.contrib.auth import views as reset_view
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('account/login/', SignInView.as_view(), name="signin"),
    path('account/register/', RegisterView.as_view(), name="signup"),
    path('account/logout/', logout, name="logout"),
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
    path('layanan/pengaduan', ReportPage, name="pengaduan"),
    path('informasi/pengumuman/', AnnouncementPage, name="pengumuman"),
    path('informasi/kegiatan/', ActivitiesPage, name="kegiatan"),
    path("password_reset/",reset_view.PasswordResetView.as_view(), name="password_reset"),
    path("password_reset/done/",reset_view.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset/<uidb64>/<token>/', reset_view.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset/done/', reset_view.PasswordResetCompleteView.as_view(), name="password_reset_complete")
]