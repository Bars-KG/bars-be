from django.urls import path

from api.views.search_recommendation import SearchRecommendationAPIView

urlpatterns = [
    path(
        "search/recommendation/",
        SearchRecommendationAPIView.as_view(),
        name="search-recommendation",
    ),
]
