from rest_framework import serializers
from .models import MetaTagsservices,Subheading


class Service_metadataSerializers(serializers.ModelSerializer):
    class Meta:
        model   =   MetaTagsservices
        fields  =   '__all__'


class subheadingSerializers(serializers.ModelSerializer):

    class Meta:
        model = Subheading
        fields = '__all__'