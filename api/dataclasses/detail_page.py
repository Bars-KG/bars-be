from typing import Optional, Union
from commons.dataclasses import BaseDataClass

class DetailFieldDataClass(BaseDataClass):
    type: str
    key: Optional[str] = None
    value: str
    hyperlink: Optional[str] = None

class DetailPageDataClass(BaseDataClass):
    title: str
    detail_fields: list[DetailFieldDataClass]