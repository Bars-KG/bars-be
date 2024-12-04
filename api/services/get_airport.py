from api.constants.continents import CONTINENTS
from api.dataclasses.detail_page import DetailPageDataClass
from api.detail_builder import detail_builder, hyperlink_field, literal_field, section_builder
from api.sparqls.get_airport import LOCAL_AIRPORT_PROPERTIES
from commons.runnable import Runnable
from store.iri import get_iri_value
from store.store import LocalStore


class GetAirportService(Runnable):
    airport_detail_builder = detail_builder([
        section_builder("Summary"),
        literal_field("IATA Code", "iataCode"),
        literal_field("Local Code", "localCode"),
        literal_field("GPS Code", "gpsCode"),
        literal_field("Scheduled Service", lambda x: "No" if x == "false" else "Yes"),
        section_builder("Geographic Location"),
        literal_field("Latitude Degree", "latitudeDegree", float),
        literal_field("Longitude Degree", "longitudeDegree", float),
        literal_field("Elevation", "elevation"),
        literal_field("Municipality", "municipality"),
        hyperlink_field("Country", "country", "countryCode", link_caster=lambda x: "/country/" + get_iri_value(x)),
        hyperlink_field("Region", "region", "regionCode", link_caster=lambda x: "/region/" + get_iri_value(x)),
        literal_field("Continent", "continentCode", lambda x: CONTINENTS[get_iri_value(x)])
    ])

    @classmethod
    def run(cls, code: str):
        local_results = LocalStore.query(LOCAL_AIRPORT_PROPERTIES, code=code)
        result = local_results[0]

        detail = cls.airport_detail_builder(result)

        return DetailPageDataClass(
            title=result["airport"]["value"],
            detail_fields=detail
        )
