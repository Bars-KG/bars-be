LOCAL_SEARCH_AIRPORTS_RESULTS = r"""
SELECT ?airport ?label ?code WHERE {{
    ?airport rdf:type :Aerodrome;
    	rdfs:label ?label ;
        verb:gpsCode ?code .
    
    FILTER(CONTAINS(LCASE(?label), "{keyword}"))
}}
"""


REMOTE_SEARCH_AIRPORTS_RESULTS = r"""
SELECT DISTINCT ?airport_code ?description ?image
WHERE {{
    VALUES ?airport_code {{ {codes} }}
    ?airport wdt:P31/wdt:P279* wd:Q62447 ;
        wdt:P239 ?airport_code .
    OPTIONAL {{
        ?airport schema:description ?description .
        FILTER(LANG(?description) = "en")
    }}
    OPTIONAL {{
        ?airport wdt:P18 ?image .
    }}
}}
"""
