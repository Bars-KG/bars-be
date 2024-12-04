from typing import Optional
from commons.dataclasses import BaseDataClass

class DetailFieldDataClass(BaseDataClass):
    type: str
    label: Optional[str] = None
    value: Optional[str] = None
    hyperlink: Optional[str] = None

class DetailPageDataClass(BaseDataClass):
    title: str
    detail_fields: list[DetailFieldDataClass]

    def extend(self, fields: list[DetailFieldDataClass]):
        self.detail_fields.extend(fields)