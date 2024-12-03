from typing import Optional, Union

from django.core.paginator import EmptyPage, Paginator
from django.db.models import QuerySet
from django.http import QueryDict
from rest_framework import serializers

from commons.dataclasses import BaseDataClass
from commons.utils import get_query_param
from commons.serializers import ReadOnlySerializer


class BasePaginationQueryParams(BaseDataClass):
    page: Optional[int] = None
    limit: Optional[int] = None


class BasePaginationDataClass(BaseDataClass):
    count_items: Optional[int] = None
    next_page: Optional[int] = None
    previous_page: Optional[int] = None


class BasePaginationSerializer(ReadOnlySerializer):
    count_items = serializers.IntegerField()
    next_page = serializers.IntegerField(allow_null=True)
    previous_page = serializers.IntegerField(allow_null=True)


class PaginationData(BaseDataClass):
    queryset: Union[QuerySet, list]
    count_items: Optional[int] = None
    next_page: Optional[int] = None
    previous_page: Optional[int] = None


def parse_pagination_params(
    params: QueryDict,
    page: Optional[int] = 1,
    limit: Optional[int] = 10
) -> BasePaginationQueryParams:
    page_val = get_query_param(params, "page")
    if page_val:
        if not page_val.isnumeric():
            raise ValueError("Page is not a number")

        page_val = int(page_val)
        if page_val > -1:
            page = page_val

    limit_val = get_query_param(params, "limit")
    if limit_val:
        if not limit_val.isnumeric():
            raise ValueError("Limit is not a number")
        
        limit_val = int(limit_val)
        if limit_val > -1:
            limit = limit_val

    return BasePaginationQueryParams(
        page=page,
        limit=limit
    )


def paginate_queryset(
    queryset: QuerySet, 
    page: Optional[int], 
    limit: Optional[int]
) -> PaginationData:
    count_items: Optional[int] = None
    next_page: Optional[int] = None
    previous_page: Optional[int] = None

    if page and limit:
        pagination = Paginator(queryset, limit)
        count_items = pagination.count
        try:
            page_data = pagination.page(page)
            try:
                next_page = page_data.next_page_number()
            except EmptyPage:
                pass
            try:
                previous_page = page_data.previous_page_number()
            except EmptyPage:
                pass
            queryset = page_data.object_list
        except EmptyPage:
            queryset = []
    elif limit:
        queryset = queryset[:limit]

    return PaginationData(
        queryset=queryset,
        count_items=count_items,
        next_page=next_page,
        previous_page=previous_page
    )
