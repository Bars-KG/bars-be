from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

from api.serializers.get_airport_countries import GetAirportCountriesResponseSerializer
from api.services.get_airport_countries import GetAirportCountriesService

from commons.exceptions import BadRequestException
from commons.paginations import parse_pagination_params


class GetAirportCountriesAPI(APIView):
    def get(self, request: Request, continent_code: str) -> Response:
        try:
            query_params = parse_pagination_params(request.GET)
        except Exception as e:
            raise BadRequestException(str(e)) from e
        
        data = GetAirportCountriesService.run(
            continent_code=continent_code,
            limit=query_params.limit,
            page=query_params.page
        )

        return Response(GetAirportCountriesResponseSerializer(data).data)
