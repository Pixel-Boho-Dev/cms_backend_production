from rest_framework import serializers
from .models import HomeHeaderCustom,AboutPageSectionCustom

class HomeHeaderCustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeHeaderCustom
        fields = "__all__"

class AboutPageSectionCustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutPageSectionCustom
        fields = "__all__"
