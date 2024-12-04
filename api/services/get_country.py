from api.builders.country_detail_builder import country_detail_builder
from api.dataclasses.detail_page import DetailPageDataClass
from api.sparqls.get_country import LOCAL_COUNTRY_PROPERTIES, REMOTE_COUNTRY_PROPERTIES
from commons.runnable import Runnable
from commons.utils import combine_query_results
from store.store import LocalStore, RemoteStore


class GetCountryService(Runnable):
    @classmethod
    def run(cls, code: str):
        local_country_results = LocalStore.query(LOCAL_COUNTRY_PROPERTIES, code=code)
        local_country_results[0]["countryCode"] = {"value": code}

        remote_country_results = RemoteStore.query(REMOTE_COUNTRY_PROPERTIES, code=code)

        country_result = combine_query_results(local_country_results, remote_country_results, "countryCode", "countryCode")[0]

        detail = country_detail_builder(country_result)

        return DetailPageDataClass(
            title=country_result["countryName"]["value"], detail_fields=detail
        )
