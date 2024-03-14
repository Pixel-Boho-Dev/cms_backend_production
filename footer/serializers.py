from rest_framework import serializers
from .models import Footer

class FooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Footer
        fields = ['id','title','location','address','email','phone_number1','phone_number2']
