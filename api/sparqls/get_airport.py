LOCAL_AIRPORT_PROPERTIES = r"""
SELECT ?airport ?iataCode ?gpsCode ?localCode ?isScheduledService ?latitude ?longitude ?elevation ?municipality ?countryCode ?country ?regionCode ?region ?continentCode
WHERE {{
    BIND(:{code} as ?a)

    ?a rdf:type :Aerodrome ;
        rdfs:label ?airport ;
    	verb:isScheduledService ?isScheduledService ;
    	verb:geographicLocation ?b .
    ?b verb:latitudeDegree ?latitude ;
    	verb:longitudeDegree ?longitude ;
    	verb:isoCountryCode ?countryCode ;
    	verb:isoRegionCode ?regionCode ;
    	verb:continentCode ?continentCode .
    ?countryCode rdfs:label ?country .
    ?regionCode rdfs:label ?region .
    
    OPTIONAL {{
        ?b verb:elevation ?elevation .
    }}
    OPTIONAL {{
        ?b verb:municipality ?municipality .
    }}
    OPTIONAL {{
        ?a verb:gpsCode ?gpsCode .
    }}
    OPTIONAL {{
        ?a verb:iataCode ?iataCode .    	
    }}
    OPTIONAL {{
        ?a verb:localCode ?localCode .
    }}
}}
"""