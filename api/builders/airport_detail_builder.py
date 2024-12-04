from api.builders.detail_builder import detail_builder, hyperlink_builder, literal_builder, section_builder
from api.constants.continents import CONTINENTS
from store.iri import get_iri_value


airport_detail_builder = detail_builder(
    [
        section_builder("Summary"),
        literal_builder("Type", "typeLabel"),
        literal_builder("IATA Code", "iataCode"),
        literal_builder("Local Code", "localCode"),
        literal_builder("GPS Code", "gpsCode"),
        literal_builder(
            "Scheduled Service", lambda x: "No" if x == "false" else "Yes"
        ),
        section_builder("Geographic Location"),
        literal_builder("Latitude Degree", "latitudeDegree", float),
        literal_builder("Longitude Degree", "longitudeDegree", float),
        literal_builder("Elevation", "elevation"),
        literal_builder("Municipality", "municipality"),
        hyperlink_builder(
            "Country",
            "country",
            "countryCode",
            link_caster=lambda x: "/country/" + get_iri_value(x),
        ),
        hyperlink_builder(
            "Region",
            "region",
            "regionCode",
            link_caster=lambda x: "/region/" + get_iri_value(x),
        ),
        literal_builder(
            "Continent", "continentCode", lambda x: CONTINENTS[get_iri_value(x)]
        ),
    ]
)

runway_detail_builder = detail_builder(
    [
        literal_builder("ID", "runway", lambda x: get_iri_value(x)),
        literal_builder("Width", "width"),
        literal_builder("Length", "length"),
        literal_builder("Surface", "surface"),
        literal_builder(
            "Lighted", "isLighted", lambda x: "No" if x == "false" else "Yes"
        ),
        literal_builder(
            "Closed", "isClosed", lambda x: "No" if x == "false" else "Yes"
        ),
        literal_builder("Low End ID", "lowEndId"),
    ]
)