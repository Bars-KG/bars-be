from api.builders.airport_detail_builder import airport_detail_builder, runway_detail_builder
from api.constants.continents import CONTINENTS
from api.dataclasses.detail_page import DetailPageDataClass
from api.builders.detail_builder import (
    section_field,
    separator_field,
)
from api.sparqls.get_airport import LOCAL_AIRPORT_PROPERTIES, LOCAL_AIRPORT_RUNWAYS
from commons.runnable import Runnable
from store.store import LocalStore


class GetAirportService(Runnable):
    @classmethod
    def run(cls, code: str):
        local_airport_results = LocalStore.query(LOCAL_AIRPORT_PROPERTIES, code=code)
        airport_result = local_airport_results[0]

        detail = airport_detail_builder(airport_result)

        local_runway_results = LocalStore.query(LOCAL_AIRPORT_RUNWAYS, code=code)

        if len(local_runway_results) > 0:
            detail.extend([section_field("Runways")])

            for idx, runway in enumerate(local_runway_results):
                detail.extend(runway_detail_builder(runway))

                if idx < len(local_runway_results) - 1:
                    detail.extend([separator_field()])

        return DetailPageDataClass(
            title=airport_result["airport"]["value"], detail_fields=detail
        )
