from rest_framework import serializers
from django.contrib.auth import authenticate

from superuser.models import Activity,Announcement, Gallery
from layanan.models import SuratKematian,SuratNikah,SuratTidakMampu,SuratPindah,SuratUsaha

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        user = authenticate(**attrs)
        if user is None:
            raise serializers.ValidationError('Invalid Credentials')

        attrs['user'] = user
        return attrs

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields="__all__"

class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields="__all__"

class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields ="__all__"

class SuratKematianSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuratKematian
        fields = "__all__"

class SuratNikahSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuratNikah
        fields="__all__"

class SuratPindahSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuratPindah
        fields="__all__"

class SuratKeteranganTidakMampuSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuratTidakMampu
        fields="__all__"

class SuratUsahaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuratUsaha
        fields="__all__"