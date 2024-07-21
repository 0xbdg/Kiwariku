from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('login/', SignInView.as_view(), name="signin"),
    path('register', RegisterView.as_view(), name="signup")
]