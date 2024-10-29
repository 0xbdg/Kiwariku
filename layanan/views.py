from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponseForbidden

from superuser.models import Citizen, Account
from .forms import *

def user_required(view_func):
    @login_required
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_superuser:
            return HttpResponseForbidden("Admin tidak berhak untuk mengakses halaman ini")
        return view_func(request, *args, **kwargs)
    return _wrapped_view

# Create your views here.

class SignInView(View):
    form_class = LoginForm
    template_name = 'pages/signin.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, context={'form': form})

    def post(self,request):
        form = self.form_class(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if not(user.is_superuser or user.is_staff):
                login(request, user)
                return redirect('profile')  # Redirect to a success page.
            else:
                form.add_error(None, 'Username atau Password anda salah!, silahkan periksa kembali')
        return render(request, self.template_name, context={"form":form})

@user_required
def ChangePasswordPage(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'pages/change_password.html', context={'form':form})

@user_required
def signout(request):
    logout(request)
    return redirect("signin")

@user_required
def ProfilePage(request):
    account = Account.objects.get(username=request.user.get_username())
    penduduk = Citizen.objects.get(akun_layanan=account)

    return render(request, "pages/profile.html", context={"profil":penduduk})

@user_required
def PengajuanPage(request):
    if request.method == "POST":
        form = PengajuanForm(data=request.POST)

        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = PengajuanForm()

    return render(request, "pages/pengajuan.html", context={'form':form})

@user_required
def PengaduanPage(request):
    return render(request, "pages/pengaduan.html")