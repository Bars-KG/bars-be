from rest_framework.views import APIView
from rest_framework.response import Response

from api.query_params_parser import parse_search_params
from api.serializers.search_recommendation import SearchRecommendationResponseSerializer
from api.services.search_recommendation import SearchRecommendationService

class SearchRecommendationAPIView(APIView):
    def get(self, request):
        query_params = parse_search_params(request.GET)

        data = SearchRecommendationService.run(**query_params.model_dump())

        return Response(SearchRecommendationResponseSerializer(data).data)