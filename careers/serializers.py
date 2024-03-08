# serializers.py
from rest_framework import serializers
from .models import CareerPage, CareerSubmission

class CareerPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareerPage
        fields = '__all__'

class CareerSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareerSubmission
        fields = '__all__'
