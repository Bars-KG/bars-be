from rest_framework import serializers

from commons.serializers import ReadOnlySerializer


class ContinentSerializer(ReadOnlySerializer):
    code = serializers.CharField()
    name = serializers.CharField()


class GetAirportContinentsResponseSerializer(ReadOnlySerializer):
    continents = ContinentSerializer(many=True)
