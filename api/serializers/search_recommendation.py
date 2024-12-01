from commons.serializers import ReadOnlySerializer
from rest_framework import serializers

class SearchRecommendationSerializer(ReadOnlySerializer):
    title = serializers.CharField()
    description = serializers.CharField(allow_null=True)
    entity = serializers.CharField()

class SearchRecommendationResponseSerializer(ReadOnlySerializer):
    recommendation = SearchRecommendationSerializer(many=True)