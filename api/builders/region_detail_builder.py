from api.builders.detail_builder import detail_builder, hyperlink_builder, image_builder, literal_builder, section_builder
from store.iri import get_iri_value

region_detail_builder = detail_builder([
    section_builder("Summary"),
    image_builder("flagImage"),
    literal_builder("Name", "regionName"),
    hyperlink_builder(
        "Country",
        "countryName",
        "country",
        link_caster=lambda x: "/country/" + get_iri_value(x),
    ),
    literal_builder("ISO Region Code", "regionCode"),
    literal_builder("Local Code", "localCode"),
    literal_builder("Capital", "capitalName"),
    section_builder("Demographic"),
    literal_builder("Area (sq. km.)", "area"),
    literal_builder("Population", "population"),
])