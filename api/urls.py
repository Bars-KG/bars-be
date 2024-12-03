from django.urls import path

from api.views.search_recommendation import SearchRecommendationAPIView
from api.views.search_results import SearchResultsAPI


urlpatterns = [
    path(
        "search/recommendation/",
        SearchRecommendationAPIView.as_view(),
        name="search-recommendation",
    ),
    path(
        "search/",
        SearchResultsAPI.as_view(),
        name="search-results"
    )
]
