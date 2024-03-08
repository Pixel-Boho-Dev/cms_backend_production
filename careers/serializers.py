# serializers.py
from rest_framework import serializers
from .models import CareerPage, CareerSubmission

class CareerPageSerializer(serializers.ModelSerializer):
    submitted_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    class Meta:
        model = CareerPage
        fields = '__all__'

class CareerSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareerSubmission
        fields = '__all__'
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['submitted_at'] = instance.submitted_at.strftime('%Y-%m-%d %H:%M')
        return representation