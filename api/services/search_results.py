from api.dataclasses.search_results import SearchResultDataClass, SearchResultsDataClass
from api.sparqls.search_results import LOCAL_SEARCH_AIRPORTS_RESULTS, REMOTE_SEARCH_AIRPORTS_RESULTS

from commons.runnable import Runnable
from commons.paginations import paginate_queryset
from commons.utils import combine_query_results

from store.store import LocalStore, RemoteStore


class SearchResultsService(Runnable):
    @classmethod
    def run(cls, keyword: str, limit: int, page: int) -> SearchResultsDataClass:
        local_results = LocalStore.query(LOCAL_SEARCH_AIRPORTS_RESULTS, keyword=keyword)
        airport_codes = " ".join([f'"{result["code"]["value"]}"' for result in local_results])

        try:
            remote_results = RemoteStore.query(REMOTE_SEARCH_AIRPORTS_RESULTS, codes=airport_codes)
        except Exception as e:
            remote_results = []

        combined_results = combine_query_results(local_results, remote_results, "code", "airport_code")

        paginated_results = paginate_queryset(
            queryset=combined_results,
            page=page,
            limit=limit
        )

        airports = [
            SearchResultDataClass(
                title=result["label"]["value"],
                description=result["description"]["value"] if "description" in result else None,
                image_url=result["image"]["value"] if "image" in result else None,
                entity=result["airport"]["value"]
            ) for result in paginated_results.queryset
        ]

        return SearchResultsDataClass(
            data=airports,
            count_items=paginated_results.count_items,
            next_page=paginated_results.next_page,
            previous_page=paginated_results.previous_page
        )
