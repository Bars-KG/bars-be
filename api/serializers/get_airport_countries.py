from rest_framework import serializers

from commons.serializers import ReadOnlySerializer
from commons.paginations import BasePaginationSerializer


class CountrySerializer(ReadOnlySerializer):
    code = serializers.CharField()
    name = serializers.CharField()


class GetAirportCountriesResponseSerializer(BasePaginationSerializer):
    data = CountrySerializer(many=True)
