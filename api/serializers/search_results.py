from rest_framework import serializers

from commons.serializers import ReadOnlySerializer
from commons.paginations import BasePaginationSerializer

class SearchResultSerializer(ReadOnlySerializer):
    title = serializers.CharField()
    description = serializers.CharField(allow_null=True)
    image_url = serializers.CharField(allow_null=True)
    entity = serializers.CharField()


class SearchResultsSerializer(BasePaginationSerializer):
    data = SearchResultSerializer(many=True)
