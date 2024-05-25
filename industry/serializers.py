from rest_framework import serializers
from .models import IndustriesPage,MetaTagsIndustries

#serializers for industries page
class IndustriesPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndustriesPage
        fields = ['id', 'title', 'subtitle', 'description', 'image', 'alt_img_text', 'alt_img_title', 'alt_img_Caption', 'alt_img_description']

#urls for industries meta   
class Industries_metadataSerializers(serializers.ModelSerializer):
    class Meta:
        model   =   MetaTagsIndustries
        fields  =   '__all__'