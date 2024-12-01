from typing import Optional
from commons.dataclasses import BaseDataClass


class SearchRecommendationDataClass(BaseDataClass):
    title: str
    description: Optional[str]
    entity: str

class SearchRecommendationListDataClass(BaseDataClass):
    recommendation: list[SearchRecommendationDataClass]