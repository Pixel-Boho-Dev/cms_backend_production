from rest_framework import serializers
from .models import ContactHeader, Section, ContactForm, MetaTagsContacts,FAQ

#serializers for contactheader
class ContactHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactHeader
        fields = '__all__'
        
#serializers for section of contact
class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'

#serializers for contactform
class ContactFormSerializer(serializers.ModelSerializer):
    timestamp = serializers.DateTimeField(format='%Y-%m-%d %H:00', read_only=True)

    class Meta:
        model = ContactForm
        fields = '__all__'

# serializers for contact page meta data.
class Contact_metadataSerializers(serializers.ModelSerializer):
    class Meta:
        model   =   MetaTagsContacts
        fields  =   '__all__'

# Serializer for frequently asked questions
class FAQSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M', read_only=True)
    updated_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M', read_only=True)
    class Meta:
        model = FAQ
        fields = ['created_at', 'updated_at']

        fields = '__all__'
