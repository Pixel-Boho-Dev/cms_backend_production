# serializers.py
from rest_framework import serializers
from .models import IndustryCard,IndustryTitles

class IndustryCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndustryCard
        fields = '__all__'


class IndustryTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndustryTitles
        fields = ['id', 'title']