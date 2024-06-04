from rest_framework import serializers
from .models import Office,Location,Location_page,MetaTagsLocation

#serializers for office

class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = [
            'id', 'location', 'place_name', 'office_address', 'fax', 'email',
            'country_manager_name', 'designation', 'country_manager_phone1',
            'country_manager_phone2', 'is_head_office', 'office_url',
            'office_description'
        ]

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

