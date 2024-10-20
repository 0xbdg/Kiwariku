from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from .forms import *
from superuser.models import *

# Create your views here.

class IndexView(View):
    template_name = "pages/index.html"
    
    def get(self, request):
        article = Blog.objects.all()[:3]
        activity = Activities.objects.all()[:3]
        announcement = Announcement.objects.all()[:3]

        if Blog.objects.count() <= 3:
            article = Blog.objects.all()

        if Activities.objects.count() <=3:
            activity = Activities.objects.all()
        
        if Announcement.objects.count() <= 3:
            announcement = Announcement.objects.all()

        return render(request, self.template_name, context={"artikel":article, "kegiatan":activity, "pengumuman":announcement})

class SignInView(View):
    form_class = LoginForm
    template_name = 'auth/signin.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, context={'form': form})

    def post(self,request):
        form = self.form_class(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("index")
        return render(request, self.template_name, context={"form":form})

@login_required
def signout(request):
    logout(request)
    return redirect("signin")

@login_required
def ProfilePage(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = ProfileForm(instance=request.user)
    return render(request,"pages/profil.html", context={'form':form})

@login_required
def ChangePasswordPage(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'auth/change_password.html', context={'form':form})
    
def HistoryPage(request):
    return render(request,"pages/sejarah.html")

def StructurePage(request):
    return render(request, "pages/struktur.html")

def NewsPage(request):
    return render(request, "pages/berita.html", context={'news':Blog.objects.all()})

def NewsDetailPage(request, news_id):
    news = Blog.objects.get(id=news_id)
    return render(request, "pages/berita_detail.html", context={'blog':news})

def ReportPage(request):
    return render(request, "pages/layanan/pengaduan.html", context={})

def AnnouncementPage(request):
    return render(request, "pages/informasi/pengumuman.html", context={})

def ActivitiesPage(request):
    return render(request, "pages/informasi/kegiatan.html", context={})

@login_required
def LayananKtpPage(request):
    if request.method == "POST":
        form = KTPForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = KTPForm()
    return render(request, "pages/pengajuan/ktp.html", context={'form':form})

@login_required
def LayananDomisiliPage(request):
    if request.method == 'POST':
        form = DomicileForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = DomicileForm()
    return render(request, "pages/pengajuan/domisili.html", context={'form':form})

@login_required
def LayananSuratCeraiPage(request):
    if request.method == 'POST':
        form = DivorceForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form=DivorceForm()
    return render(request, "pages/pengajuan/surat_cerai.html", context={'form':form})

@login_required
def LayananSuratNikahPage(request):
    if request.method == 'POST':
        form = MarriageForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MarriageForm()
    return render(request, "pages/pengajuan/surat_nikah.html",context={'form':form})