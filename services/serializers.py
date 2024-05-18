from rest_framework import serializers
from .models import MetaTagsservices,Subheading,SpecializedService,SpecializedSubService

class Service_metadataSerializers(serializers.ModelSerializer):
    class Meta:
        model   =   MetaTagsservices
        fields  =   '__all__'

class subheadingSerializers(serializers.ModelSerializer):

    class Meta:
        model = Subheading
        fields = '__all__'

class SpecializedServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecializedService
        fields = '__all__'

class SpecializedSubServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecializedSubService
        fields = '__all__'