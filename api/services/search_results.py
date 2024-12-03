from typing import Optional, Any

from api.dataclasses.search_results import SearchResultDataClass, SearchResultsDataClass
from api.sparqls.search_results import (
    LOCAL_SEARCH_AIRPORTS_RESULTS_WITH_FILTER_BY_COUNTRY,
    LOCAL_SEARCH_AIRPORTS_RESULTS_WITHOUT_FILTER_BY_COUNTRY,
    LOCAL_AIRPORTS_FILTER_BY_COUNTRY,
    REMOTE_SEARCH_AIRPORTS_RESULTS
)

from commons.runnable import Runnable
from commons.paginations import paginate_queryset
from commons.utils import combine_query_results

from store.store import LocalStore, RemoteStore


class SearchResultsService(Runnable):
    @classmethod
    def run(cls, keyword: str, limit: int, page: int, country: Optional[str] = None) -> SearchResultsDataClass:
        keyword = keyword.lower()
        if country is None:
            local_results = LocalStore.query(
                LOCAL_SEARCH_AIRPORTS_RESULTS_WITHOUT_FILTER_BY_COUNTRY, keyword=keyword)
        elif keyword != "":
            local_results = LocalStore.query(
                LOCAL_SEARCH_AIRPORTS_RESULTS_WITH_FILTER_BY_COUNTRY, 
                keyword=keyword, 
                country_code=country
            )
        else:
            local_results = LocalStore.query(LOCAL_AIRPORTS_FILTER_BY_COUNTRY, country_code=country)

        paginated_results = paginate_queryset(
            queryset=local_results,
            page=page,
            limit=limit
        )

        results_qs = paginated_results.queryset
        airport_codes = " ".join([f'"{result["code"]["value"]}"' for result in results_qs])
        try:
            remote_results = RemoteStore.query(REMOTE_SEARCH_AIRPORTS_RESULTS, codes=airport_codes)
        except Exception:
            remote_results = []
        
        combined_results = combine_query_results(results_qs, remote_results, "code", "airport_code")

        airports = [
            SearchResultDataClass(
                title=result["label"]["value"],
                type=result["airport_type_labels"]["value"],
                description=cls.__get_noneable_value(result, "description"),
                country=cls.__get_noneable_value(result, "country"),
                country_label=cls.__get_noneable_value(result, "country_label"),
                city=cls.__get_noneable_value(result, "city"),
                city_label=cls.__get_noneable_value(result, "city_label"),
                image_url=cls.__get_noneable_value(result, "image"),
                entity=result["airport"]["value"]
            ) for result in combined_results
        ]

        return SearchResultsDataClass(
            data=airports,
            count_items=paginated_results.count_items,
            next_page=paginated_results.next_page,
            previous_page=paginated_results.previous_page
        )
    
    @classmethod
    def __get_noneable_value(cls, data: Any, key: str) -> Optional[str]:
        return data[key]["value"] if key in data else None
