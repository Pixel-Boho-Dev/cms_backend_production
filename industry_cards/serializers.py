# serializers.py
from rest_framework import serializers
from .models import IndustryCard



class IndustryCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndustryCard
        fields = '__all__'
