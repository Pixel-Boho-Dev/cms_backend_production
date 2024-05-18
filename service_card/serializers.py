from rest_framework import serializers
from .models import ServicesCard,ServiceTitle

class ServicesCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicesCard
        fields = '__all__'

class ServiceTitleSerializer(serializers.ModelSerializer):  # Change here
    class Meta:
        model = ServiceTitle
        fields = '__all__'