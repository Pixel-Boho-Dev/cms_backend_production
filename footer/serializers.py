# serializers.py

from rest_framework import serializers
from .models import Footer

class AppFooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Footer
        fields = ['id', 'icon', 'location', 'address', 'email', 'phone_number1', 'phone_number2']
