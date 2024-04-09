from rest_framework import serializers
from .models import key_diffrentiates, key_diffrentiatesSection

class key_diffrentiatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = key_diffrentiates
        fields = ['id', 'icon', 'tagline']

class key_diffrentiatesSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = key_diffrentiatesSection
        fields = ['id', 'title', 'subtitle']  # Adjust the fields as needed
