from rest_framework import serializers
from .models import SocialMedia,Service,Location,Achievement,HomeHighlights,Industry,Market,MetaTagsHome,AchievementSection,HighlightsSection,MarketTitle,OurNetworkTitle
from services.models import SubService
from services.serializers import subheadingSerializers
from django.db import models


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
    subservices = SubServiceSerializer(many=True, read_only=True)   
    class Meta:
        model = Service
        fields = '__all__'

#serializer for serviceheader
class ServiceheaderSerializer(serializers.ModelSerializer):
    class Meta:
        model= Service
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

#models for ournetwork title
class OurNetworkTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurNetworkTitle
        fields = '__all__'

# serializers for achievements
class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = '__all__'
    def validate_order_by(self, value):
        if self.instance is None and Achievement.objects.filter(order_by=value).exists():
            raise serializers.ValidationError("Already exist.")
        return value

    def create(self, validated_data):
        order_by = validated_data.get('order_by')
        if Achievement.objects.filter(order_by=order_by).exists():
            raise serializers.ValidationError({"order_by": ["Already exist."]})
        return super().create(validated_data)

    def update(self, instance, validated_data):
        new_order = validated_data.get('order_by', instance.order_by)
        
        # Get the current order_by value of the instance
        current_order = instance.order_by

        # If the new order is different from the current order, perform update
        if new_order != current_order:
            # Adjust order_by values of other instances if necessary
            if new_order > current_order:
                Achievement.objects.filter(order_by__gt=current_order, order_by__lte=new_order).update(order_by=models.F('order_by') - 1)
            elif new_order < current_order:
                Achievement.objects.filter(order_by__lt=current_order, order_by__gte=new_order).update(order_by=models.F('order_by') + 1)

        return super().update(instance, validated_data)


#serializers for acheievement title
class AchievementSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AchievementSection
        fields = ['id','title']

# serializers for highlights
class HighlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeHighlights
        fields = '__all__'

#serializers for highlight title
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

#serializers for market title
class MarketTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketTitle
        fields = ['id','title']

# serializers for Metatags home
class MetaTagsHomeSerializer(serializers.ModelSerializer):
    class Meta:
        model= MetaTagsHome
        fields = '__all__'

