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
class ourstoryCustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ourstoryCustom
        fields = "__all__"

#serializers for milestone

class milestoneCustomserializers(serializers.ModelSerializer):
    class Meta:
        model = milestoneCustom
        fields = "__all__"

#serializers for ourteam

class ourteamCustomserializers(serializers.ModelSerializer):
    class Meta:
        model = ourteamCustom
        fields = "__all__"

#serializers for whatweare
class whatweareCustomserializers(serializers.ModelSerializer):
    class Meta:
        model = whatweareCustom
        fields = "__all__"
#serializers for certification
class certificationCustomserializers(serializers.ModelSerializer):
    class Meta:
        model = certificationCustom
        fields = "__all__"

#serializers for contactform
class contactformCustomserializers(serializers.ModelSerializer):
    class Meta:
        model = contactformCustom
        fields = "__all__"

#serializers for footer
class footerCustomserializers(serializers.ModelSerializer):
    class Meta:
        model = footerCustom
        fields = "__all__"

#serializers for headerournetwork
class headerournetworkCustomserializers(serializers.ModelSerializer):
    class Meta:
        model = headerournetworkCustom
        fields = "__all__"

#serializers for ournetworkdescription       
class ournetworkdescriptionCustomSerializers(serializers.ModelSerializer):
    class Meta:
        model = ournetworkdescriptionCustom
        fields = "__all__"

#serializers for ournetworklocation       
class ournetworklocationCustomSerializers(serializers.ModelSerializer):
    class Meta:
        model = ournetworklocationCustom
        fields = "__all__"

#serializers for ournetworklocation       
class ournetworkofficesCustomSerializers(serializers.ModelSerializer):
    class Meta:
        model = ournetworkofficesCustom
        fields = "__all__"





