from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import IsAuthenticated

from .serializers import *

# Create your views here.

class LoginView(APIView):
    renderer_classes = [JSONRenderer]
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)

class SuratKematianUploadView(APIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [JSONRenderer]
    def post(self, request, *args, **kwargs):
        serializer = SuratKematianSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SuratNikahUploadView(APIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [JSONRenderer]
    def post(self, request, *args, **kwargs):
        serializer = SuratNikahSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SuratPindahUploadView(APIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [JSONRenderer]
    def post(self, request, *args, **kwargs):
        serializer = SuratPindahSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SuratUsahaUploadView(APIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [JSONRenderer]
    def post(self, request, *args, **kwargs):
        serializer = SuratUsahaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SuratTidakMampuUploadView(APIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [JSONRenderer]
    def post(self, request, *args, **kwargs):
        serializer = SuratKeteranganTidakMampuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class KegiatanView(APIView):
    renderer_classes = [JSONRenderer]
    def get(self, request):
        kegiatan = Activity.objects.all()
        s = ActivitySerializer(kegiatan, many=True)
        return Response(s.data)

class PengumumanView(APIView):
    renderer_classes = [JSONRenderer]
    def get(self, request):
        pengumuman = Announcement.objects.all()
        s = ActivitySerializer(pengumuman, many=True)
        return Response(s.data)