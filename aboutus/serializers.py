from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.db import models
from .models import AboutPageSection,OurStory,Milestone,OurTeam,WhatWeAre,Certifications,MetaTagsAbout,CertificateTitle,OurTeamTitle,MilestoneTitle,WhatWeAreTitle

#serializer for aboutpagesection
class AboutPageSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutPageSection
        fields = '__all__'

#serializer for ourstory
class OurStorySerializer(serializers.ModelSerializer):
    class Meta:
        model = OurStory
        fields = '__all__'

#serializer for milestone
class MilestoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Milestone
        fields = '__all__'

#serializer for milestonetitle
class MilestoneTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MilestoneTitle
        fields = ['id','title','sub_title']

#serializer for ourteam
class OurTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurTeam
        fields = '__all__'

    def validate_order_by(self, value):
        if self.instance is None and OurTeam.objects.filter(order_by=value).exists():
            raise serializers.ValidationError("Already exist.")
        return value

    def create(self, validated_data):
        order_by = validated_data.get('order_by')
        if OurTeam.objects.filter(order_by=order_by).exists():
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
                OurTeam.objects.filter(order_by__gt=current_order, order_by__lte=new_order).update(order_by=models.F('order_by') - 1)
            elif new_order < current_order:
                OurTeam.objects.filter(order_by__lt=current_order, order_by__gte=new_order).update(order_by=models.F('order_by') + 1)

        return super().update(instance, validated_data)

#serializer for ourteamtitle
class OurTeamTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurTeamTitle
        fields = '__all__'

#serializer for whatweare
class WhatWeAreSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhatWeAre
        fields='__all__'

#serializer for certification
class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Certifications
        fields='__all__'

#serializer for certification title
class CertificateTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CertificateTitle
        fields = ['id','title']

#serializer for aboutmeta
class About_metadataSerializers(serializers.ModelSerializer):
    class Meta:
        model   =   MetaTagsAbout
        fields  =   '__all__'

#serializer for whatweare title
class WhatWeAreTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhatWeAreTitle
        fields = ['id','title']