from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('login/', SignInView.as_view(), name="signin"),
    path('register/', RegisterView.as_view(), name="signup"),
    path('sejarah/', HistoryPage, name="sejarah"),
    path('struktur/', StructurePage, name="struktur"),
    path('berita/',NewsPage, name="berita")
]