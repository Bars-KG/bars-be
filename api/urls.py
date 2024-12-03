from django.urls import path

from api.views.get_airport_continents import GetAirportContinentsAPI
from api.views.get_airport_countries import GetAirportCountriesAPI
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
    ),
    path(
        "airports/continents/",
        GetAirportContinentsAPI.as_view(),
        name="get-airport-continents"
    ),
    path(
        "airports/continents/<str:continent_code>/",
        GetAirportCountriesAPI.as_view(),
        name="get-airport-regions"
    )
]
