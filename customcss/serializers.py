from rest_framework import serializers
from .models import *

#serializers for headersection
class HomeHeaderCustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeHeaderCustom
        fields = "__all__"

#serializers for servicecard    
class ServicecardCustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicecardsCustom
        fields = "__all__"

#serializers for chooseus
class ChooseusCustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChooseusCustom
        fields ="__all__"

#serializers for ournetwork
class OurnetworkCustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurnetworkCustom
        fields = "__all__"

#serializers for keydiffrentiators
class KeydiffrentiatorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeydiffrentiatorsCustom
        fields = "__all__"

#serializers for Acheievements
class AcheievementCustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcheievementCustom
        fields = "__all__"

#serializers for highlights
class HighlightsCustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = HighlightsCustom
        fields = "__all__"

#serializers for industriescards
class IndustriesCardsCustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndustriesCardsCustom
        fields = "__all__"

#serializers for marketsupdates
class MarketUpdatesCustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketUpdatesCustom
        fields = "__all__"

#serializers for aboutpagesction
class AboutPageSectionCustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutPageSectionCustom
        fields = "__all__"

#serializers for ourstorysection
class OurstoryCustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurnetworkCustom
        fields = "__all__"

#serializers for milestone
class MilestoneCustomserializers(serializers.ModelSerializer):
    class Meta:
        model = MilestoneCustom
        fields = "__all__"

#serializers for ourteam
class OurteamCustomserializers(serializers.ModelSerializer):
    class Meta:
        model = OurteamCustom
        fields = "__all__"

#serializers for whatweare
class WhatweareCustomserializers(serializers.ModelSerializer):
    class Meta:
        model = WhatweareCustom
        fields = "__all__"

#serializers for certification
class CertificationCustomserializers(serializers.ModelSerializer):
    class Meta:
        model = CertificationCustom
        fields = "__all__"

#serializers for contactform
class ContactformCustomserializers(serializers.ModelSerializer):
    class Meta:
        model = ContactformCustom
        fields = "__all__"

#serializers for footer
class FooterCustomserializers(serializers.ModelSerializer):
    class Meta:
        model = FooterCustom
        fields = "__all__"

#serializers for headerournetwork
class HeaderournetworkCustomserializers(serializers.ModelSerializer):
    class Meta:
        model = HeaderournetworkCustom
        fields = "__all__"

#serializers for ournetworkdescription       
class OurnetworkdescriptionCustomSerializers(serializers.ModelSerializer):
    class Meta:
        model = OurnetworkdescriptionCustom
        fields = "__all__"

#serializer of service
class ServiceCustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCustom
        fields = "__all__"

        
#serializers for ournetworklocation       
class OurnetworklocationCustomSerializers(serializers.ModelSerializer):
    class Meta:
        model = OurnetworklocationCustom
        fields = "__all__"

#serializers for ournetworkoffices     
class OurnetworkofficesCustomSerializers(serializers.ModelSerializer):
    class Meta:
        model = OurnetworkofficesCustom
        fields = "__all__"
        
#serializers for careerspage      
class CareerspageCustomSerializers(serializers.ModelSerializer):
    class Meta:
        model = CareerspageCustom
        fields = "__all__"

#serializers for industriesblock 
class IndustriesBlockCustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndustriesBlocksCustom
        fields = "__all__"

#serializers for Industriespage       
class IndustriesHeaderCustomSerializer(serializers.ModelSerializer):
    blocks = IndustriesBlockCustomSerializer(many=True, read_only=True)
    class Meta:
        model = IndustriesHeaderCustom
        fields = "__all__"