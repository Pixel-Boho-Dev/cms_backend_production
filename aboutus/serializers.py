from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.db import models

from .models import AboutPageSection,OurStory,Milestone,OurTeam,WhatWeAre,Certifications,MetaTagsAbout,CertificateTitle,OurTeamTitle,WhatWeAreTitle,MilestoneTitle



class AboutPageSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutPageSection
        fields = '__all__'


class OurStorySerializer(serializers.ModelSerializer):
    class Meta:
        model = OurStory
        fields = '__all__'

class MilestoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Milestone
        fields = '__all__'

class MilestoneTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MilestoneTitle
        fields = ['id','title','sub_title']

class OurTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurTeam
        fields = '__all__'
    
    
    def update(self, instance, validated_data):
        new_order = validated_data.get('order_by', instance.order_by)

        # Get the current order_by value of the instance
        current_order = instance.order_by

        # If the new order is greater than the current order,
        # move all objects with order_by values between current_order and new_order down by 1
        if new_order > current_order:
            OurTeam.objects.filter(order_by__gt=current_order, order_by__lte=new_order).update(order_by=models.F('order_by') - 1)

        # If the new order is less than the current order,
        # move all objects with order_by values between new_order and current_order up by 1
        elif new_order < current_order:
            OurTeam.objects.filter(order_by__lt=current_order, order_by__gte=new_order).update(order_by=models.F('order_by') + 1)

        return super().update(instance, validated_data)


class OurTeamTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurTeamTitle
        fields = '__all__'


class WhatWeAreSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhatWeAre
        fields='__all__'

class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Certifications
        fields='__all__'

class CertificateTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CertificateTitle
        fields = ['id','title']

class About_metadataSerializers(serializers.ModelSerializer):
    class Meta:
        model   =   MetaTagsAbout
        fields  =   '__all__'

class WhatWeAreTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhatWeAreTitle
        fields = ['id','title']
