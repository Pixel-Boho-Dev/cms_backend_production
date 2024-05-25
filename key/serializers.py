from rest_framework import serializers
from .models import key_diffrentiates, key_diffrentiatesSection

#serializer for keydifrrentiates
class key_diffrentiatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = key_diffrentiates
        fields = ['id', 'icon', 'tagline']

#serializer for keydiffrentiates title
class key_diffrentiatesSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = key_diffrentiatesSection
        fields = ['id', 'title', 'subtitle']  # Adjust the fields as needed
