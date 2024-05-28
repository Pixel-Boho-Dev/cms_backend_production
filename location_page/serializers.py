from rest_framework import serializers
from .models import Office,Location,Location_page,MetaTagsLocation

#serializers for office
class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = '__all__'

#serializers for location_page
class Location_pageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location_page
        fields='__all__'

# serializers for Location page meta data
class Location_metadataSerializers(serializers.ModelSerializer):
    class Meta:
        model   =   MetaTagsLocation
        fields  =   '__all__'

