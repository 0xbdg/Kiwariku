from django.urls import path
from django.contrib.auth import views as reset_view
from .views import *

urlpatterns = [
    path('profil/', ProfilePage, name="profile"),
    path('account/login/', SignInView.as_view(), name="signin"),
    path('account/logout/', logout, name="logout"),
    path('account/change_password', ChangePasswordPage, name="change"),
    path("password_reset/",reset_view.PasswordResetView.as_view(), name="password_reset"),
    path("password_reset/done/",reset_view.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset/<uidb64>/<token>/', reset_view.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset/done/', reset_view.PasswordResetCompleteView.as_view(), name="password_reset_complete")
]
