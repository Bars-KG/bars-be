from django.http import QueryDict
from commons.dataclasses import BaseDataClass
from commons.utils import get_query_param


class SearchQueryParams(BaseDataClass):
    keyword: str

def parse_search_params(params: QueryDict) -> SearchQueryParams:
    keyword = get_query_param(params, "keyword")
    if keyword is None:
        raise ValueError("Invalid keyword")
    
    return SearchQueryParams(keyword=keyword)