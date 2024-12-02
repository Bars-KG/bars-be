from api.dataclasses.search_recommendation import SearchRecommendationDataClass, SearchRecommendationListDataClass
from api.sparql import LOCAL_SEARCH_AIRPORTS_RECOMMENDATION, REMOTE_SEARCH_AIRPORTS_RECOMMENDATION
from commons.runnable import Runnable
from commons.utils import combine_query_results
from store.store import LocalStore, RemoteStore


class SearchRecommendationService(Runnable):
    @classmethod
    def run(cls, keyword: str):
        local_results = LocalStore.query(LOCAL_SEARCH_AIRPORTS_RECOMMENDATION, keyword=keyword)

        airport_codes = " ".join([f'"{result["code"]["value"]}"' for result in local_results])
        
        remote_results = RemoteStore.query(REMOTE_SEARCH_AIRPORTS_RECOMMENDATION, codes=airport_codes)

        combined_results = combine_query_results(local_results, remote_results, "code", "airport_code")

        airports = [
            SearchRecommendationDataClass(
                title=result["label"]["value"],
                description=result["description"]["value"] if "description" in result else None,
                entity=result["airport"]["value"]
            ) for result in combined_results
        ]

        return SearchRecommendationListDataClass(recommendation=airports)