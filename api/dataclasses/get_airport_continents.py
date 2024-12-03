from typing import List

from commons.dataclasses import BaseDataClass


class ContinentDataClass(BaseDataClass):
    code: str
    name: str


class ContinentListDataClass(BaseDataClass):
    continents: List[ContinentDataClass]
