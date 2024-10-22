from django.shortcuts import render
from django.views.generic import View
from django.conf import settings
from superuser.models import *

import requests,datetime
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
    
def IndexDesaMembangun(request):
    IKS = 0
    IKE = 0
    IKL = 0

    api = f"http://idm.kemendesa.go.id/open/api/desa/rumusan/{settings.ID_DESA}/{datetime.datetime.now().year}"

    req = requests.get(api)
    data = req.json()

    for l in data["mapData"]["ROW"]:
        if l["ROW_CELL"] == 45:
            IKS = l["SKOR"]
        if l["ROW_CELL"] == 58:
            IKE = l["SKOR"]
        if l["ROW_CELL"] == 62:
            IKL = l["SKOR"]
    
    RESULT = (IKS+IKE+IKL)
    IKS_PERCENT = IKS * 100 / RESULT
    IKE_PERCENT = IKE * 100 / RESULT
    IKL_PERCENT = IKL * 100 / RESULT

    magma_composition_data = [
        {"label":"IKS","symbol":"O","y": IKS_PERCENT},
        {"label":"IKE","symbol":"Si","y": IKE_PERCENT},
        {"label":"IKL","symbol":"Al","y": IKL_PERCENT},
    ]

    return render(request, "pages/idm.html", context={
        'status':data["mapData"]["SUMMARIES"]["STATUS"], 
        "skor":round(data["mapData"]["SUMMARIES"]["SKOR_SAAT_INI"],4), 
        "target":data["mapData"]["SUMMARIES"]["TARGET_STATUS"], 
        "minimal":data["mapData"]["SUMMARIES"]["SKOR_MINIMAL"],
        "tahun":data["mapData"]["SUMMARIES"]["TAHUN"],
        "magma_composition_data" : magma_composition_data 
    })

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
    return render(request, "pages/informasi/pengaduan.html", context={})

def AnnouncementPage(request):
    return render(request, "pages/informasi/pengumuman.html", context={})

def ActivitiesPage(request):
    return render(request, "pages/informasi/kegiatan.html", context={})