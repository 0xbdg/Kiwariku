from rest_framework import serializers

from superuser.models import Activity,Announcement

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields="__all__"

class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields="__all__"