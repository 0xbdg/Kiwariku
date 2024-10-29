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
        activity = Activity.objects.all()[:3]
        announcement = Announcement.objects.all()[:3]
        penduduk_perempuan = Citizen.objects.filter(jenis_kelamin="PEREMPUAN").count()
        penduduk_laki = Citizen.objects.filter(jenis_kelamin="LAKI-LAKI").count()
        penduduk_keseluruhan = penduduk_laki + penduduk_perempuan

        if Blog.objects.count() <= 3:
            article = Blog.objects.all()

        if Activity.objects.count() <=3:
            activity = Activity.objects.all()
        
        if Announcement.objects.count() <= 3:
            announcement = Announcement.objects.all()

        return render(request, self.template_name, context={"artikel":article, "kegiatan":activity, "pengumuman":announcement, "laki":penduduk_laki, "perempuan":penduduk_perempuan, "penduduk_semua":penduduk_keseluruhan})
    
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
    return render(request,"pages/tentang/sejarah.html")

def StructurePage(request):
    return render(request, "pages/tentang/struktur.html")

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

def VisimisiPage(request):
    return render(request, "pages/tentang/visimisi.html", context={})

def PemerintahdesaPage(request):
    return render(request,"pages/informasi/pemerintahan.html", context={})

def DataPendidikanPage(request):
    tidak_sekolah = Citizen.objects.filter(pendidikan="TIDAK SEKOLAH").count()
    sd = Citizen.objects.filter(pendidikan="SD").count()
    smp = Citizen.objects.filter(pendidikan="SMP").count()
    sma = Citizen.objects.filter(pendidikan="SMA").count()
    smk = Citizen.objects.filter(pendidikan="SMK").count()
    sltp = Citizen.objects.filter(pendidikan="SLTP").count()
    slta = Citizen.objects.filter(pendidikan="SLTA").count()
    diploma1 = Citizen.objects.filter(pendidikan="D-1").count()
    diploma2 = Citizen.objects.filter(pendidikan="D-2").count()
    diploma3 = Citizen.objects.filter(pendidikan="D-3").count()
    diploma4 = Citizen.objects.filter(pendidikan="D-4").count()
    sarjana1 = Citizen.objects.filter(pendidikan="S-1").count()
    sarjana2 = Citizen.objects.filter(pendidikan="S-2").count()
    sarjana3 = Citizen.objects.filter(pendidikan="S-3").count()

    data_pendidikan = [
        { "label": "TS", "y": tidak_sekolah },
        { "label": "SD", "y": sd },
        { "label": "SMP", "y": smp },
        { "label": "SMA", "y": sma },
        { "label": "SMK", "y": smk },
        { "label": "SLTP", "y": sltp },
        { "label": "SLTA", "y": slta },
        { "label": "D-1", "y": diploma1 },
        { "label": "D-2", "y": diploma2 },
        { "label": "D-3", "y": diploma3 },
        { "label": "D-4", "y": diploma4 },
        { "label": "S-1", "y": sarjana1 },
        { "label": "S-2", "y": sarjana2 },
        { "label": "S-3", "y": sarjana3 },
    ]

    return render(request, "pages/data/pendidikan.html", context={ "data_pendidikan" : data_pendidikan})

def DataPekerjaanPage(request):
    tidak_bekerja = Citizen.objects.filter(pekerjaan="TIDAK BEKERJA").count()
    karyawan = Citizen.objects.filter(pekerjaan="KARYAWAN").count()
    pensiunan = Citizen.objects.filter(pekerjaan="PENSIUNAN").count()
    pelajar = Citizen.objects.filter(pekerjaan="PELAJAR/MAHASISWA").count()
    art = Citizen.objects.filter(pekerjaan="ASISTEN RUMAH TANGGA").count()
    mrt = Citizen.objects.filter(pekerjaan="MENGURUS RUMAH TANGGA").count()
    wiraswasta = Citizen.objects.filter(pekerjaan="WIRASWASTA").count()
    satpam = Citizen.objects.filter(pekerjaan="SATPAM/SECURITY").count()
    barber = Citizen.objects.filter(pekerjaan="BARBER").count()
    montir = Citizen.objects.filter(pekerjaan="MONTIR").count()
    ahli_las = Citizen.objects.filter(pekerjaan="AHLI LAS/PANDAI BESI").count()
    buruh = Citizen.objects.filter(pekerjaan="BURUH").count()
    abdi_negara = Citizen.objects.filter(pekerjaan="ABDI NEGARA").count()
    petugas_kebersihan = Citizen.objects.filter(pekerjaan="PETUGAS KEBERSIHAN").count()
    nelayan = Citizen.objects.filter(pekerjaan="NELAYAN").count()
    pemuka_agama = Citizen.objects.filter(pekerjaan="PEMUKA AGAMA").count()
    wirausaha = Citizen.objects.filter(pekerjaan="WIRAUSAHA").count()
    sopir = Citizen.objects.filter(pekerjaan="SOPIR").count()
    peternak = Citizen.objects.filter(pekerjaan="PETERNAK").count()
    pengrajin = Citizen.objects.filter(pekerjaan="PENGRAJIN").count()
    digitalpreneur = Citizen.objects.filter(pekerjaan="DIGITALPRENEUR").count()
    arsitek = Citizen.objects.filter(pekerjaan="ARSITEK").count()
    pekerja_kasar = Citizen.objects.filter(pekerjaan="PEKERJA KASAR").count()
    tukang = Citizen.objects.filter(pekerjaan="TUKANG").count()
    data_pekerjaan = [
        { "label": "Tidak Bekerja", "y": tidak_bekerja },
        { "label": "Karyawan", "y": karyawan },
        { "label": "Pensiunan", "y": pensiunan },
        { "label": "Pelajar/Mahasiswa", "y": pelajar },
        { "label": "Asisten Rumah Tangga", "y": art },
        { "label": "Mengurus Rumah Tangga", "y": mrt },
        { "label": "Wiraswasta", "y": wiraswasta },
        { "label": "Satpam/Security", "y": satpam },
        { "label": "Barber", "y":  barber},
        { "label": "Montir", "y": montir },
        { "label": "Ahli Las", "y": ahli_las },
        { "label": "Buruh", "y": buruh },
        { "label": "Abdi Negara", "y": abdi_negara },
        { "label": "Petugas Kebersihan", "y": petugas_kebersihan },
        { "label": "Nelayan", "y": nelayan },
        { "label": "Pemuka Agama", "y": pemuka_agama },
        { "label": "Wirausaha", "y": wirausaha },
        { "label": "Sopir", "y": sopir },
        { "label": "Peternak", "y": peternak },
        { "label": "Pengrajin", "y": pengrajin },
        { "label": "Digitalpreneur", "y": digitalpreneur },
        { "label": "Arsitek", "y": arsitek },
        { "label": "Pekerja Kasar", "y": pekerja_kasar },
        { "label": "Tukang", "y": tukang },
    ]
    
    return render(request, "pages/data/pekerjaan.html", context={ "data_pekerjaan" : data_pekerjaan})

def DataAgamaPage(request):
    penduduk_buddha = Citizen.objects.filter(agama="BUDDHA").count()
    penduduk_hindu = Citizen.objects.filter(agama="HINDU").count()
    penduduk_islam = Citizen.objects.filter(agama="ISLAM").count()
    penduduk_kristen = Citizen.objects.filter(agama="KRISTEN").count()
    penduduk_katolik = Citizen.objects.filter(agama="KATOLIK").count()
    penduduk_konghucu = Citizen.objects.filter(agama="KONGHUCU").count()

    jumlah_semua = (penduduk_buddha+penduduk_hindu+penduduk_islam+penduduk_katolik+penduduk_kristen+penduduk_konghucu)

    data_agama = [
        { "label": "Buddha", "y": penduduk_buddha},
        { "label": "Hindu", "y": penduduk_hindu},
        { "label": "Islam", "y": penduduk_islam },
        { "label": "Katolik", "y": penduduk_katolik},
        { "label": "Kristen", "y": penduduk_kristen},
        { "label": "Konghucu", "y": penduduk_konghucu}
    ]
    
    return render(request, "pages/data/agama.html", context={ "data_agama" : data_agama})

def DataDesaPage(request):
    tidak_sekolah = Citizen.objects.filter(pendidikan="TIDAK SEKOLAH").count()
    sd = Citizen.objects.filter(pendidikan="SD").count()
    smp = Citizen.objects.filter(pendidikan="SMP").count()
    sma = Citizen.objects.filter(pendidikan="SMA").count()
    smk = Citizen.objects.filter(pendidikan="SMK").count()
    sltp = Citizen.objects.filter(pendidikan="SLTP").count()
    slta = Citizen.objects.filter(pendidikan="SLTA").count()
    diploma1 = Citizen.objects.filter(pendidikan="D-1").count()
    diploma2 = Citizen.objects.filter(pendidikan="D-2").count()
    diploma3 = Citizen.objects.filter(pendidikan="D-3").count()
    diploma4 = Citizen.objects.filter(pendidikan="D-4").count()
    sarjana1 = Citizen.objects.filter(pendidikan="S-1").count()
    sarjana2 = Citizen.objects.filter(pendidikan="S-2").count()
    sarjana3 = Citizen.objects.filter(pendidikan="S-3").count()

    data_pendidikan = [
        { "label": "TS", "y": tidak_sekolah },
        { "label": "SD", "y": sd },
        { "label": "SMP", "y": smp },
        { "label": "SMA", "y": sma },
        { "label": "SMK", "y": smk },
        { "label": "SLTP", "y": sltp },
        { "label": "SLTA", "y": slta },
        { "label": "D-1", "y": diploma1 },
        { "label": "D-2", "y": diploma2 },
        { "label": "D-3", "y": diploma3 },
        { "label": "D-4", "y": diploma4 },
        { "label": "S-1", "y": sarjana1 },
        { "label": "S-2", "y": sarjana2 },
        { "label": "S-3", "y": sarjana3 },
    ]
    return render(request, "pages/informasi/data.html", context={"data_pendidikan":data_pendidikan})