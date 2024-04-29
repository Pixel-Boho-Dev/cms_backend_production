from rest_framework import serializers
from .models import ServicesCard

class ServicesCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicesCard
        fields = '__all__'