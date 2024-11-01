from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("app.urls")),
    path('cctv/', include('cctv.urls')),
    path('layanan/', include("layanan.urls")),
    path("ckeditor/", include('django_ckeditor_5.urls')),
    path("__reload__/", include("django_browser_reload.urls")),
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)