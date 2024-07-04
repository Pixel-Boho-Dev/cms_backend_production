from rest_framework import serializers
from .models import key_diffrentiates, key_diffrentiatesSection
from django.db import models

#serializer for keydifrrentiates
class key_diffrentiatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = key_diffrentiates
        fields = ['id', 'icon', 'tagline','order_by']

    def validate_order_by(self, value):
        if self.instance is None and key_diffrentiates.objects.filter(order_by=value).exists():
            raise serializers.ValidationError("Already exist.")
        return value

    def create(self, validated_data):
        order_by = validated_data.get('order_by')
        if key_diffrentiates.objects.filter(order_by=order_by).exists():
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
                key_diffrentiates.objects.filter(order_by__gt=current_order, order_by__lte=new_order).update(order_by=models.F('order_by') - 1)
            elif new_order < current_order:
                key_diffrentiates.objects.filter(order_by__lt=current_order, order_by__gte=new_order).update(order_by=models.F('order_by') + 1)

        return super().update(instance, validated_data)

#serializer for keydiffrentiates title
class key_diffrentiatesSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = key_diffrentiatesSection
        fields = ['id', 'title', 'subtitle']  # Adjust the fields as needed
