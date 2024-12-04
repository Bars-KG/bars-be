LOCAL_SEARCH_AIRPORTS_RECOMMENDATION = r"""
SELECT ?airport ?label ?code WHERE {{
    ?airport rdf:type :Aerodrome;
    	rdfs:label ?label ;
        verb:gpsCode ?code .
    
    FILTER(CONTAINS(LCASE(?label), LCASE("{keyword}")))
}}
LIMIT 5
"""

REMOTE_SEARCH_AIRPORTS_RECOMMENDATION = r"""
SELECT DISTINCT ?airport_code ?description
WHERE {{
    VALUES ?airport_code {{ {codes} }}
    ?airport wdt:P31/wdt:P279* wd:Q62447 ;
        wdt:P239 ?airport_code .
    OPTIONAL {{
        ?airport schema:description ?description .
        FILTER(LANG(?description) = "en")
    }}
}}
"""
