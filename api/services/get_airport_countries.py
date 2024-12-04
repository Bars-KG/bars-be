from api.dataclasses.get_airport_countries import CountryDataClass, CountryListDataClass
from api.sparqls.get_airport_countries import LOCAL_GET_AIRPORT_COUNTRIES

from commons.runnable import Runnable
from commons.paginations import paginate_queryset

from store.store import LocalStore


class GetAirportCountriesService(Runnable):
    @classmethod
    def run(cls, continent_code: str, limit: int, page: int) -> CountryListDataClass:
        local_countries = LocalStore.query(LOCAL_GET_AIRPORT_COUNTRIES, continent_code=continent_code)
        paginated_countries = paginate_queryset(
            queryset=local_countries,
            page=page,
            limit=limit
        )

        countries = [
            CountryDataClass(
                code=country["country"]["value"].split('/')[-1],
                name=country["name"]["value"]
            ) for country in paginated_countries.queryset
        ]

        return CountryListDataClass(
            data=countries,
            count_items=paginated_countries.count_items,
            next_page=paginated_countries.next_page,
            previous_page=paginated_countries.previous_page
        )
