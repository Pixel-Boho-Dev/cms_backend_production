from rest_framework import serializers
from .models import MetaTagsservices


class Service_metadataSerializers(serializers.ModelSerializer):
    class Meta:
        model   =   MetaTagsservices
        fields  =   '__all__'