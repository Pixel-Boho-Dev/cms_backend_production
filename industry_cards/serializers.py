# serializers.py
from rest_framework import serializers
from .models import IndustryCard,IndustryTitles

#serializer for industrycard
class IndustryCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndustryCard
        fields = '__all__'

#serializer for industrytitle
class IndustryTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndustryTitles
        fields = ['id', 'title']