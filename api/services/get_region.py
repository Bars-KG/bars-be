from api.builders.region_detail_builder import region_detail_builder
from api.dataclasses.detail_page import DetailPageDataClass
from api.sparqls.get_region import LOCAL_REGION_PROPERTIES, REMOTE_REGION_PROPERTIES
from commons.runnable import Runnable
from commons.utils import combine_query_results
from store.store import LocalStore, RemoteStore


class GetRegionService(Runnable):
    @classmethod
    def run(cls, code: str):
        local_region_results = LocalStore.query(LOCAL_REGION_PROPERTIES, code=code)
        local_region_results[0]["regionCode"] = {"value": code}

        remote_region_results = RemoteStore.query(REMOTE_REGION_PROPERTIES, code=code)

        region_result = combine_query_results(local_region_results, remote_region_results, "regionCode", "regionCode")[0]

        detail = region_detail_builder(region_result)

        return DetailPageDataClass(
            title=region_result["regionName"]["value"], detail_fields=detail
        )
