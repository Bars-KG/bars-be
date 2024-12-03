from typing import Optional

from django.http import QueryDict

from commons.paginations import BasePaginationQueryParams, parse_pagination_params
from commons.utils import get_query_param


class SearchQueryParams(BasePaginationQueryParams):
    keyword: str
    country: Optional[str]


def parse_search_params(params: QueryDict) -> SearchQueryParams:
    keyword = get_query_param(params, "keyword", "")
    country = get_query_param(params, "country", None)
    pagination_params = parse_pagination_params(params=params)
    
    return SearchQueryParams(
        keyword=keyword,
        country=country,
        page=pagination_params.page,
        limit=pagination_params.limit
    )
