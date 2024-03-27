from rest_framework import serializers
from .models import IndustriesPage,MetaTagsIndustries

class IndustriesPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndustriesPage
        fields = '__all__'



class Industries_metadataSerializers(serializers.ModelSerializer):
    class Meta:
        model   =   MetaTagsIndustries
        fields  =   '__all__'