from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

from api.services.get_airport_continents import GetAirportContinentsService
from api.serializers.get_airport_continents import GetAirportContinentsResponseSerializer


class GetAirportContinentsAPI(APIView):
    def get(self, request: Request) -> Response:
        data = GetAirportContinentsService.run()

        return Response(GetAirportContinentsResponseSerializer(data).data)
