from commons.serializers import ReadOnlySerializer
from rest_framework import serializers


class DetailFieldDataClass(ReadOnlySerializer):
    type = serializers.CharField()
    key = serializers.CharField(allow_null=True)
    value = serializers.CharField()
    hyperlink = serializers.CharField(allow_null=True)

class DetailPageSerializer(ReadOnlySerializer):
    title = serializers.CharField()
    detail_fields = DetailFieldDataClass(many=True)