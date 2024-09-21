from django.urls import path
from .views import *

urlpatterns = [
    path('', signin, name="login"),
    path('dashboard/', dashboard, name="dashboard")
]
