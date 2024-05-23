from rest_framework import serializers
from .models import HomeHeaderCustom

class HomeHeaderCustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeHeaderCustom
        fields = "__all__"