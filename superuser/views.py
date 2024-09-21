from django.shortcuts import render
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="login")
def dashboard(request):
    return render(request, 'pages/dashboard.html', context={})

def signin(request):
    return render(request, 'auth/login.html', context={})