from rest_framework.views import APIView
from rest_framework.response import Response

from api.serializers.detail_page import DetailPageSerializer
from api.services.get_airport import GetAirportService

class GetAirportAPI(APIView):
    def get(self, request, code):
        data = GetAirportService.run(code)

        return Response(DetailPageSerializer(data).data)