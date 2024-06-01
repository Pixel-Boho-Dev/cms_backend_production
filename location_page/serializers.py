from rest_framework import serializers
from .models import Office,Location,Location_page,MetaTagsLocation

#serializers for office
class OfficeSerializer(serializers.ModelSerializer):
    phone_numbers = serializers.SerializerMethodField()

    class Meta:
        model = Office
        fields = ['id', 'location', 'place_name', 'office_address', 'fax', 'email', 
                  'country_manager_name', 'designation', 'country_manager_phone1', 
                  'country_manager_phone2', 'is_head_office', 'office_url', 
                  'office_description', 'phone_numbers']

    def get_phone_numbers(self, obj):
        phone_numbers = [obj.country_manager_phone1]
        if obj.country_manager_phone2:
            phone_numbers.append(obj.country_manager_phone2)
        return f"Tel No: {', '.join(phone_numbers)}"

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

