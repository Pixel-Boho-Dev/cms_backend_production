from rest_framework import serializers
from .models import AboutPageSection,OurStory,Milestone,OurTeam,WhatWeAre,Certifications,MetaTagsAbout,CertificateTitle

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

class OurTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurTeam
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