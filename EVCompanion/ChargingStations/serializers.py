from rest_framework import serializers
from ChargingStations.models import ChargingStation

class ChargingStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChargingStation
        fields = '__all__'