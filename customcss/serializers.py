from rest_framework import serializers
from .models import HomeHeaderCustom ,ServicecardsCustom
from .models import HomeHeaderCustom,AboutPageSectionCustom,ourstoryCustom,milestoneCustom,ournetworkCustom


#serializers for headersection

class HomeHeaderCustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeHeaderCustom
        fields = "__all__"

#serializers for aboutpagesction

class AboutPageSectionCustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutPageSectionCustom
        fields = "__all__"


#serializers for servicecard
       
class ServicecardCustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicecardsCustom
        fields = "__all__"



#serializers for ourstorysection

class ourstoryCustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ourstoryCustom
        fields = "__all__"

#serializers for milestone

class milestoneCustomserializers(serializers.ModelSerializer):
    class Meta:
        model = milestoneCustom
        fields = "__all__"

#serializers for ournetwork

class ournetworkCustomserializers(serializers.ModelSerializer):
    class Meta:
        model = ournetworkCustom
        fields = "__all__"
