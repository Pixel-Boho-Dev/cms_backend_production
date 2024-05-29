from rest_framework import serializers
from .models import ChoosesSection

#serializers for chooses
class ChoosesSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChoosesSection
        fields = ['id','title', 'subtitle', 'bg_image']
