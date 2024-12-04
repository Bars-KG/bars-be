from abc import ABC
from bars.settings import TRIPLESTORE_DATABASES

from SPARQLWrapper import SPARQLWrapper, JSON

from store.iri import get_sparql_prefixes

class Store(ABC):
    @classmethod
    def _init(cls, connection_string):
        cls.sparql = SPARQLWrapper(connection_string)
        cls.sparql.setReturnFormat(JSON)

    @classmethod
    def query(cls, query: str, **kwargs) -> list[dict]:
        query = query.format(**kwargs)
        cls.sparql.setQuery(query)
        ret = cls.sparql.queryAndConvert()

        return ret["results"]["bindings"]

class LocalStore(Store):
    @classmethod
    def _init(cls):
        super()._init(TRIPLESTORE_DATABASES["local"]["URL"])

    @classmethod
    def query(cls, query: str, **kwargs) -> list[dict]:
        query = fr"""
        {get_sparql_prefixes()}

        """ + query

        return super().query(query, **kwargs)

class RemoteStore(Store):
    @classmethod
    def _init(cls):
        super()._init(TRIPLESTORE_DATABASES["remote"]["URL"])

LocalStore._init()
RemoteStore._init()