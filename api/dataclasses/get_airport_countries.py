from typing import List

from commons.dataclasses import BaseDataClass
from commons.paginations import BasePaginationDataClass


class CountryDataClass(BaseDataClass):
    code: str
    name: str


class CountryListDataClass(BasePaginationDataClass):
    data: List[CountryDataClass]
