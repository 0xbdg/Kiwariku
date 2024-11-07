from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import *

# Create your views here.

@api_view(['GET'])
def Kegiatan(request):
    kegiatan = Activity.objects.all()
    s = ActivitySerializer(kegiatan, many=True)
    return Response(s.data)

@api_view(['GET'])
def Pengumuman(request):
    pengumuman = Announcement.objects.all()
    s = AnnouncementSerializer(pengumuman, many=True)
    return Response(s.data)

@api_view(['GET'])
def Galeri(request):
    galeri = Gallery.objects.all()
    s = AnnouncementSerializer(galeri, many=True)
    return Response(s.data)