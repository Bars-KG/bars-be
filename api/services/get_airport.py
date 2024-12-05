from api.builders.airport_detail_builder import (
    airport_detail_builder,
    runway_detail_builder,
    navaid_detail_builder,
)
from api.constants.continents import CONTINENT_WIKIDATA
from api.dataclasses.detail_page import DetailPageDataClass
from api.builders.detail_builder import (
    section_field,
    separator_field,
)
from api.sparqls.get_airport import (
    LOCAL_AIRPORT_NAVAIDS,
    LOCAL_AIRPORT_PROPERTIES,
    LOCAL_AIRPORT_RUNWAYS,
    REMOTE_AIRPORT_PROPERTIES,
)
from commons.runnable import Runnable
from commons.utils import combine_query_results
from store.store import LocalStore, RemoteStore


class GetAirportService(Runnable):
    @classmethod
    def run(cls, code: str):
        local_airport_results = LocalStore.query(LOCAL_AIRPORT_PROPERTIES, code=code)

        remote_airport_results = RemoteStore.query(REMOTE_AIRPORT_PROPERTIES, code=code)

        airport_result = combine_query_results(
            local_airport_results, remote_airport_results, "gpsCode", "airport_code"
        )[0]

        detail = airport_detail_builder(airport_result)

        local_runway_results = LocalStore.query(LOCAL_AIRPORT_RUNWAYS, code=code)

        local_navaid_results = LocalStore.query(LOCAL_AIRPORT_NAVAIDS, code=code)

        if len(local_runway_results) > 0:
            detail.extend([section_field("Runways")])

            for idx, runway in enumerate(local_runway_results):
                detail.extend(runway_detail_builder(runway))

                if idx < len(local_runway_results) - 1:
                    detail.extend([separator_field()])

        if len(local_navaid_results) > 0:
            detail.extend([section_field("Navigation Aids")])

            for idx, navaid in enumerate(local_navaid_results):
                detail.extend(navaid_detail_builder(navaid))

                if idx < len(local_navaid_results) - 1:
                    detail.extend([separator_field()])

        return DetailPageDataClass(
            title=airport_result["airport"]["value"], detail_fields=detail
        )
