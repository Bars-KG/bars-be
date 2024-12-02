from typing import Any, Optional
from django.http import QueryDict


def get_query_param(queries: QueryDict, key: str, default: Any = None) -> Optional[str]:
    val = queries.get(key, default)
    if type(val) is str:
        if len(val) == 0:
            return default
    return val


def combine_query_results(
    result1: list[dict], result2: list[dict], on1: str, on2: str
) -> list[dict]:
    return [
        {**x, **(next((y for y in result2 if x[on1]["value"] == y[on2]["value"]), {}))}
        for x in result1
    ]
