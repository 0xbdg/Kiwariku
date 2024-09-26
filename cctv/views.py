from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .forms import *

# Create your views here.
def signin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user.is_superuser or user.is_staff:
                login(request, user)
                return redirect('camera')  # Redirect to a success page.
            else:
                # Invalid login
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'login_cctv.html', {'form': form})

@login_required(login_url="/cctv/login")
def index(request):
    return render(request, 'index_cctv.html')