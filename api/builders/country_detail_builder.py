from datetime import datetime
from api.builders.detail_builder import detail_builder, hyperlink_builder, image_builder, literal_builder, section_builder
from api.constants.continents import CONTINENTS
from store.iri import get_iri_value


country_detail_builder = detail_builder(
    [
        section_builder("Summary"),
        image_builder("flagImage"),
        hyperlink_builder("Capital", "capitalName", "capital"),
        literal_builder(
            "Inception Date",
            "inception",
            lambda x: datetime.strptime(x, "%Y-%m-%dT%H:%M:%SZ").strftime("%d %B %Y"),
        ),
        hyperlink_builder("Head of State", "headOfStateName", "headOfState"),
        hyperlink_builder("Currency", "currencyName", "currency"),
        literal_builder(
            "Continent", "continent", lambda x: CONTINENTS[get_iri_value(x)]
        ),
        section_builder("Demographic"),
        literal_builder("Population", "population"),
        literal_builder("Area (sq. mi.)", "area"),
        literal_builder("Population Density (per sq. mi.)", "density"),
        section_builder("Economy"),
        literal_builder("GDP", "gdp"),
        literal_builder("Agriculture", "agriculture"),
        literal_builder("Service", "service"),
        literal_builder("Industry", "industry"),
        section_builder("Health"),
        literal_builder("Net Migration", "netMigration"),
        literal_builder("Infant Mortality", "infantMortality"),
        literal_builder("Birthrate", "birthrate"),
        literal_builder("Deathrate", "deathrate"),
        section_builder("Land Usage"),
        literal_builder("Arable (%)", "arableLand"),
        literal_builder("Crops (%)", "cropsLand"),
        literal_builder("Other (%)", "otherLand"),
        section_builder("Other"),
        literal_builder("Literacy (%)", "literacy"),
        literal_builder("Phones (per 1000)", "phoneDensity"),
        literal_builder("Coastline/Area Ratio", "coastline"),
    ]
)
