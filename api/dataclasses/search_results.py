from typing import Optional, List

from commons.dataclasses import BaseDataClass
from commons.paginations import BasePaginationDataClass


class SearchResultDataClass(BaseDataClass):
    title: str
    description: Optional[str]
    image_url: Optional[str]
    entity: str


class SearchResultsDataClass(BasePaginationDataClass):
    data: List[SearchResultDataClass]
