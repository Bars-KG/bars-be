from api.constants.continents import CONTINENTS
from api.dataclasses.get_airport_continents import ContinentDataClass, ContinentListDataClass
from api.sparqls.get_airport_continents import LOCAL_GET_AIRPORT_CONTINENT_CODES

from commons.runnable import Runnable

from store.store import LocalStore


class GetAirportContinentsService(Runnable):
    @classmethod
    def run(cls) -> ContinentListDataClass:
        local_continent_codes = LocalStore.query(LOCAL_GET_AIRPORT_CONTINENT_CODES)

        if len(local_continent_codes) == 0:
            return ContinentListDataClass(continents=[])
        
        continent_codes = [item['continent_code']['value'].split('/')[-1] for item in local_continent_codes]
        
        continents = [
            ContinentDataClass(
                code=continent,
                name=CONTINENTS[continent]
            ) for continent in continent_codes
        ]

        return ContinentListDataClass(continents=continents)
