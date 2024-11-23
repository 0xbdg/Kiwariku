from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from datetime import datetime
from django_ckeditor_5.fields import CKEditor5Field
import uuid

# Create your models here.

GENDER = (
    ("LAKI-LAKI","Laki-Laki"),
    ("PEREMPUAN", "Perempuan")
)

RELIGION = (
    ("BUDDHA", "Buddha"),
    ("KRISTEN", "Kristen"),
    ("ISLAM", "Islam"),
    ("KATOLIK", "Katolik"),
    ("HINDU", "Hindu"),
    ("KONGHUCU", "Konghucu")
)

EDUCATION = (
    ("TIDAK SEKOLAH","Tidak Sekolah"),
    ("SD","SD"),
    ("SMP", "SMP"),
    ("SMA", "SMA"),
    ("SMK", "SMK"),
    ("SLTP", "SLTP"),
    ("SLTA", "SLTA"),
    ("D-1", "D1"),
    ("D-2", "D2"),
    ("D-3", "D3"),
    ("D-4", "D4"),
    ("S-1", "S1"),
    ("S-2", "S2"),
    ("S-3", "S3")
)

JOB = (
    ("TIDAK BEKERJA", "Tidak Bekerja"),
    ("KARYAWAN", "Karyawan"),
    ("PENSIUNAN", "Pensiunan"),
    ("PELAJAR/MAHASISWA", "Pelajar/Mahasiswa"),
    ("MENGURUS RUMAH TANGGA", "Mengurus Rumah Tangga"),
    ("ASISTEN RUMAH TANGGA", "Asisten Rumah Tangga"),
    ("WIRASWASTA", "Wiraswasta"),
    ("SATPAM/SECURITY", "Satpam/Security"),
    ("BARBER", "Barber"),
    ("MONTIR", "Montir"),
    ("AHLI LAS/PANDAI BESI", "Ahli Las/Pandai Besi"),
    ("BURUH", "Buruh"),
    ("ABDI NEGARA", "Abdi Negara"),
    ("PETUGAS KEBERSIHAN", "Petugas Kebersihan"),
    ("NELAYAN", "Nelayan"),
    ("PEMUKA AGAMA", "Pemuka Agama"),
    ("WIRAUSAHA", "Wirausaha"),
    ("SOPIR", "Sopir"),
    ("PETERNAK", "Peternak"),
    ("PENGRAJIN", "Pengrajin"),
    ("DIGITALPRENEUR", "Digitalpreneur"),
    ("ARSITEK", "Arsitek"),
    ("PEKERJA KASAR", "Pekerja Kasar"),
    ("TUKANG", "Tukang")
)

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, email, password, **extra_fields)

class Account(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(default=datetime.now())

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    # Specify unique related names for groups and user_permissions
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='account_set',
        related_query_name='account',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='account_set',
        related_query_name='account',
    )

    def __str__(self):
       return self.username
    
    class Meta:
        verbose_name = "Akun"
        verbose_name_plural = "Akun"

class Blog(models.Model):
    id = models.CharField(primary_key=True, default=uuid.uuid4, editable=False, max_length=36)
    thumbnail = models.ImageField(upload_to="thumbnail/")
    title = models.CharField(max_length=255, null=False, unique=True)
    description = models.CharField(max_length=255, null=False, unique=True, blank=False)
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    content = CKEditor5Field("Content", config_name="extends")
    upload_date = models.DateTimeField(auto_now_add=datetime.now(), editable=False)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Artikel"
        verbose_name_plural = "Artikel Desa"
    
class Announcement(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=False)
    date = models.DateTimeField(auto_now_add=datetime.now())

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Pengumuman"
        verbose_name_plural = "Pengumuman Desa"

class Activity(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=False)
    location = models.CharField(blank=False, max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    upload_date = models.DateTimeField(auto_now_add=datetime.now())

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Kegiatan"
        verbose_name_plural = "Kegiatan Desa"
    
class Citizen(models.Model):
    NIK = models.CharField(max_length=16, null=False, blank=False, unique=True)
    KK = models.CharField(max_length=16, null=False, blank=False, unique=True)
    akun_layanan = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, blank=True)
    nama_lengkap = models.CharField(max_length=255, null=False, blank=False)
    tempat_lahir = models.CharField(max_length=255, null=False, blank=False)
    RT = models.IntegerField(null=False, blank=False)
    RW = models.IntegerField(null=False, blank=False)
    tanggal_lahir = models.DateField(null=False, blank=False)
    alamat = models.CharField(max_length=500, null=False, blank=False)
    agama = models.CharField(max_length=255,choices=RELIGION, null=False, blank=False)
    jenis_kelamin = models.CharField(max_length=255, choices=GENDER, null=False,blank=False)
    pendidikan = models.CharField(max_length=255,choices=EDUCATION, null=False, blank=False)
    pekerjaan = models.CharField(max_length=255,choices=JOB, null=False, blank=False)

    def __str__(self):
        return self.nama_lengkap
    
    class Meta:
        verbose_name = "Penduduk"
        verbose_name_plural = "Penduduk Desa"

class Aparatur(models.Model):
    foto_pemerintah = models.ImageField(upload_to="foto_pemerintahan_desa/")
    nama_orang = models.CharField(max_length=255)
    jabatan = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.nama_orang
    
    class Meta:
        verbose_name = "Aparatur"
        verbose_name_plural = "Aparatur Desa"

class Gallery(models.Model):
    image = models.ImageField(upload_to="galeri/")
    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name="Galeri"
        verbose_name_plural = "Galeri Desa"

class Bantuan(models.Model):
    JENIS_BANTUAN = (
        ("BLT", "BLT"),
        ("PKH", "PKH"),
        ("STUNTING", "STUNTING"),
        ("BPJS", "BPJS"),
        ("BPNT", "BPNT"),
        ("BANSOS", "BANSOS")
    )

    bulan = (
        ("01", "01"),
        ("02", "02"),
        ("03", "03"),
        ("04", "04"),
        ("05", "05"),
        ("06", "06"),
        ("07", "07"),
        ("08", "08"),
        ("09", "09"),
        ("10", "10"),
        ("11", "11"),
        ("12", "12"),
    )

    tahun = (
        ("2024", "2024"),
        ("2025", "2025"),
        ("2026", "2026"),
        ("2027", "2027"),
        ("2028", "2028"),
    )
    jenis_bantuan = models.CharField(choices=JENIS_BANTUAN, max_length=10)    
    nama_bantuan = models.CharField(max_length=1000)
    nilai = models.DecimalField(max_digits=30, decimal_places=2)
    jumlah = models.DecimalField(max_digits=30, decimal_places=0)
    total = models.DecimalField(max_digits=30, decimal_places=2)
    bulan = models.CharField(choices=bulan,max_length=2)
    tahun = models.CharField(choices=tahun, max_length=4)
    tanggal_input = models.DateField()

    def __str__(self):
        return self.nama_bantuan
    
    class Meta:
        verbose_name = "Bantuan"
        verbose_name_plural = "Bantuan Desa"