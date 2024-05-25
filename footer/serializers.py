from rest_framework import serializers
from .models import Footer

#serializer for footer
class FooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Footer
        fields = "__all__"
