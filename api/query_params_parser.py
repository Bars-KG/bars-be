from django.http import QueryDict

from commons.paginations import BasePaginationQueryParams, parse_pagination_params
from commons.utils import get_query_param


class SearchQueryParams(BasePaginationQueryParams):
    keyword: str


def parse_search_params(params: QueryDict) -> SearchQueryParams:
    keyword = get_query_param(params, "keyword", "")
    pagination_params = parse_pagination_params(params=params)
    
    return SearchQueryParams(
        keyword=keyword,
        page=pagination_params.page,
        limit=pagination_params.limit
    )
