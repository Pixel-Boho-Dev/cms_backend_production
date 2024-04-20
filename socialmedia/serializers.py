from rest_framework import serializers
from .models import SocialMedia,Service,Location,Achievement,HomeHighlights,Industry,Market,Home,MetaTagsHome,AchievementSection,HighlightsSection,MarketTitle
from services.models import SubService
from services.serializers import subheadingSerializers

# serializers for social media
class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = '__all__'

# serializers for subservices
class SubServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubService
        fields = '__all__'
# serializer for services
class ServiceSerializer(serializers.ModelSerializer):
    subheadings = subheadingSerializers(many=True,read_only=True)
    subservices = SubServiceSerializer(many=True, read_only=True)  # Nested representation
    class Meta:
        model = Service
        fields = '__all__'

# serializers for retriving subservices of a service
class ServiceheadingSubServiceSerializer(serializers.Serializer):
    service = ServiceSerializer()
    subheading = subheadingSerializers(many = True)
    subservices = SubServiceSerializer(many=True)

# serializers for location
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

# serializers for achievements

class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = '__all__'

class AchievementSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AchievementSection
        fields = ['id','title']

# serializers for highlights
class HighlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeHighlights
        fields = '__all__'

class HighlightsSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HighlightsSection
        fields =['id','title']

# serializers for Industries

class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = '__all__'

# serializers for Market News

class MarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Market
        fields = '__all__'

class MarketTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketTitle
        fields = ['id','title']

# serializers for Home details

class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = '__all__'

# serializers for Metatags home
class MetaTagsHomeSerializer(serializers.ModelSerializer):
    class Meta:
        model= MetaTagsHome
        fields = '__all__'

