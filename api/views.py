from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.renderers import JSONRenderer

from .serializers import *

# Create your views here.

class SuratKematianUploadView(APIView):
    renderer_classes = [JSONRenderer]
    def post(self, request, *args, **kwargs):
        serializer = SuratKematianSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SuratNikahUploadView(APIView):
    renderer_classes = [JSONRenderer]
    def post(self, request, *args, **kwargs):
        serializer = SuratNikahSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SuratPindahUploadView(APIView):
    renderer_classes = [JSONRenderer]
    def post(self, request, *args, **kwargs):
        serializer = SuratPindahSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SuratUsahaUploadView(APIView):
    renderer_classes = [JSONRenderer]
    def post(self, request, *args, **kwargs):
        serializer = SuratUsahaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SuratTidakMampuUploadView(APIView):
    renderer_classes = [JSONRenderer]
    def post(self, request, *args, **kwargs):
        serializer = SuratKeteranganTidakMampuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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