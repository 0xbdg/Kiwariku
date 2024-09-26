from django.urls import path
from .views import *

urlpatterns = [
    path('login_cctv', signin, name="login_cctv"),
    path('home', index, name="camera")
]
