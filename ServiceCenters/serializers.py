# serializers.py
from rest_framework import serializers
from .models import ServiceCenter, Service, DeliveryBoy

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'name', 'price']


class ServiceCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCenter
        fields = '__all__'


class DeliveryBoySerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryBoy
        fields = ['id', 'first_name', 'last_name', 'phone_number', 'email', 'address']