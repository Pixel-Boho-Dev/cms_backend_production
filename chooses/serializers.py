from rest_framework import serializers
from .models import ChoosesSection

class ChoosesSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChoosesSection
        fields = ['title', 'subtitle', 'bg_image']
