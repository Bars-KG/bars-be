from abc import ABC
from bars.settings import TRIPLESTORE_DATABASES

from SPARQLWrapper import SPARQLWrapper, JSON

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
        query = r"""
        PREFIX : <http://data.bars-kg.com/entity/>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX verb: <http://data.bars-kg.com/verb/>

        """ + query

        return super().query(query, **kwargs)

class RemoteStore(Store):
    @classmethod
    def _init(cls):
        super()._init(TRIPLESTORE_DATABASES["remote"]["URL"])

LocalStore._init()
RemoteStore._init()