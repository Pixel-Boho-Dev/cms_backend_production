from rest_framework import serializers
from .models import HomeHeader

class HeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeHeader
        fields = ['id','title','subtitle','description','image']
        ref_name = 'HeaderContact' 
