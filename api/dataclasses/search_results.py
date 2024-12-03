from typing import Optional, List

from commons.dataclasses import BaseDataClass
from commons.paginations import BasePaginationDataClass


class SearchResultDataClass(BaseDataClass):
    title: str
    type: str
    description: Optional[str]
    country: Optional[str]
    country_label: Optional[str]
    city: Optional[str]
    city_label: Optional[str]
    image_url: Optional[str]
    entity: str


class SearchResultsDataClass(BasePaginationDataClass):
    data: List[SearchResultDataClass]
