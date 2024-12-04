from rest_framework.views import APIView
from rest_framework.response import Response

from api.serializers.detail_page import DetailPageSerializer
from api.services.get_region import GetRegionService

class GetRegionAPI(APIView):
    def get(self, request, code):
        data = GetRegionService.run(code)

        return Response(DetailPageSerializer(data).data)