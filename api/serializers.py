from rest_framework import serializers

from superuser.models import Activity,Announcement, Gallery

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