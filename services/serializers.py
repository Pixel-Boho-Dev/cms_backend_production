from rest_framework import serializers
from .models import MetaTagsservices,Subheading,SpecializedService,SpecializedSubService

#serializer for servicemeta
class Service_metadataSerializers(serializers.ModelSerializer):
    class Meta:
        model   =   MetaTagsservices
        fields  =   '__all__'

#serializer for subheading
class subheadingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Subheading
        fields = '__all__'

#serializer for specialized service
class SpecializedServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecializedService
        fields = '__all__'

#serializer for specializedsubservice
class SpecializedSubServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecializedSubService
        fields = '__all__'
