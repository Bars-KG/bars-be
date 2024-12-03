LOCAL_SEARCH_AIRPORTS_RESULTS_WITHOUT_FILTER_BY_COUNTRY = r"""
SELECT ?airport ?label ?code ?country_label (GROUP_CONCAT(DISTINCT ?airport_type_label; separator=", ") AS ?airport_type_labels) WHERE {{
    ?airport rdf:type :Aerodrome;
    	rdfs:label ?label ;
        verb:gpsCode ?code ;
        verb:geographicLocation ?geographic_location ;
        a ?airport_type .
    
    ?geographic_location verb:isoCountryCode ?iso_country_code .
    ?iso_country_code rdfs:label ?country_label .
        
    ?airport_type rdfs:label ?airport_type_label .

    FILTER(CONTAINS(LCASE(?label), "{keyword}"))
}}
GROUP BY ?airport ?label ?code ?country_label
ORDER BY ?label
"""


LOCAL_AIRPORTS_FILTER_BY_COUNTRY = r"""
SELECT ?airport ?label ?code (GROUP_CONCAT(DISTINCT ?airport_type_label; separator=", ") AS ?airport_type_labels) WHERE {{
    ?airport rdf:type :Aerodrome;
    	rdfs:label ?label ;
        verb:gpsCode ?code ;
        verb:geographicLocation ?geographic_location ;
        a ?airport_type .
    
    ?geographic_location verb:isoCountryCode :{country_code} .
        
    ?airport_type rdfs:label ?airport_type_label .
}}
GROUP BY ?airport ?label ?code
ORDER BY ?label
"""


LOCAL_SEARCH_AIRPORTS_RESULTS_WITH_FILTER_BY_COUNTRY = r"""
SELECT ?airport ?label ?code ?country_label (GROUP_CONCAT(DISTINCT ?airport_type_label; separator=", ") AS ?airport_type_labels) WHERE {{
    ?airport rdf:type :Aerodrome;
    	rdfs:label ?label ;
        verb:gpsCode ?code ;
        verb:geographicLocation ?geographic_location ;
        a ?airport_type .
    
    ?geographic_location verb:isoCountryCode :{country_code} .
        
    ?airport_type rdfs:label ?airport_type_label .

    FILTER(CONTAINS(LCASE(?label), "{keyword}"))
}}
GROUP BY ?airport ?label ?code ?country_label
ORDER BY ?label
"""


REMOTE_SEARCH_AIRPORTS_RESULTS = r"""
SELECT ?airport_code ?city ?city_label ?country ?country_label ?description ?image
WHERE {{
    VALUES ?airport_code {{ {codes} }}
    ?airport wdt:P31/wdt:P279* wd:Q62447 ;
        wdt:P239 ?airport_code ;
        wdt:P131 ?city ;
        wdt:P17 ?country .
    
    ?city rdfs:label ?city_label .
    FILTER(LANG(?city_label) = "en")

    ?country rdfs:label ?country_label .
    FILTER(LANG(?country_label) = "en")

    OPTIONAL {{
        ?airport schema:description ?description .
        FILTER(LANG(?description) = "en")
    }}

    OPTIONAL {{
        ?airport wdt:P18 ?image .
    }}
}}
"""
