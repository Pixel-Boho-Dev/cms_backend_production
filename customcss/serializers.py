from rest_framework import serializers
from .models import HomeHeaderCustom ,ServicecardsCustom

class HomeHeaderCustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeHeaderCustom
        fields = "__all__"

class ServicecardCustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicecardsCustom
        fields = "__all__"