from rest_framework import serializers

from commons.serializers import ReadOnlySerializer
from commons.paginations import BasePaginationSerializer

class SearchResultSerializer(ReadOnlySerializer):
    title = serializers.CharField()
    type = serializers.CharField()
    description = serializers.CharField(allow_null=True)
    country = serializers.CharField(allow_null=True)
    country_label = serializers.CharField(allow_null=True)
    city = serializers.CharField(allow_null=True)
    city_label = serializers.CharField(allow_null=True)
    image_url = serializers.CharField(allow_null=True)
    entity = serializers.CharField()


class SearchResultsSerializer(BasePaginationSerializer):
    data = SearchResultSerializer(many=True)
