from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

from api.query_params_parser import parse_search_params
from api.services.search_results import SearchResultsService
from api.serializers.search_results import SearchResultsSerializer

from commons.exceptions import BadRequestException


class SearchResultsAPI(APIView):
    def get(self, request: Request) -> Response:
        try:
            query_params = parse_search_params(request.GET)
        except Exception as e:
            raise BadRequestException(str(e)) from e

        data = SearchResultsService.run(
            keyword=query_params.keyword,
            limit=query_params.limit,
            page=query_params.page
        )
    
        return Response(SearchResultsSerializer(data).data)
