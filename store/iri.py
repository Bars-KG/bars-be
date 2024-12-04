IRIS = {
    ":": "http://data.bars-kg.com/entity/",
    "rdf:": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "rdfs:": "http://www.w3.org/2000/01/rdf-schema#",
    "verb:": "http://data.bars-kg.com/verb/"
}

def get_sparql_prefixes() -> str:
    return "\n".join([f"PREFIX {prefix} <{IRIS[prefix]}>" for prefix in IRIS])

def get_iri_string(prefixed: str) -> str:
    prefix, fragment = prefixed.split(":")
    return IRIS[prefix + ":"] + fragment

def get_prefixed_iri(iri_string: str) -> str:
    for prefix in IRIS:
        if iri_string.startswith(IRIS[prefix]):
            return prefix + iri_string.split(IRIS[prefix])[1]

def get_iri_value(iri_string: str) -> str:
    for prefix in IRIS:
        if iri_string.startswith(IRIS[prefix]):
            return iri_string.split(IRIS[prefix])[1]