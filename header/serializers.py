from rest_framework import serializers
from .models import HomeHeader

class HeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeHeader
        fields = '__all__'
        ref_name = 'HeaderContact' 
