from rest_framework import serializers
from .models import key_diffrentiates

class key_diffrentiatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = key_diffrentiates
        fields = ['title', 'subtitle', 'icon', 'tagline']
