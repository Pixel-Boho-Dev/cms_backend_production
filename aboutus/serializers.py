from rest_framework import serializers

from .models import AboutPageSection,OurStory,Milestone,OurTeam,WhatWeAre,Certifications,MetaTagsAbout,CertificateTitle,OurTeamTitle,MilestoneTitle,WhatWeAreTitle



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
    
    
    def create(self, validated_data):
        # Calculate order_by based on the number of existing objects + 1
        validated_data['order_by'] = OurTeam.objects.count() + 1
        return super().create(validated_data)


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
