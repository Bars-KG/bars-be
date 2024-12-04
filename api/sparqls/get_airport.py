LOCAL_AIRPORT_PROPERTIES = r"""
SELECT ?airport ?typeLabel ?iataCode ?gpsCode ?localCode ?isScheduledService ?latitude ?longitude ?elevation ?municipality ?countryCode ?country ?regionCode ?region ?continentCode
WHERE {{
    BIND(:{code} as ?a)

    ?a rdf:type :Aerodrome ;
        rdfs:label ?airport ;
    	verb:isScheduledService ?isScheduledService ;
    	verb:geographicLocation ?b ;
        rdf:type ?type .
    ?type rdfs:label ?typeLabel .
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

    FILTER NOT EXISTS {{
        ?a rdf:type ?type2 .
        ?type2 rdfs:subClassOf ?type .
        FILTER(?type2 != ?type)
    }}
}}
"""

REMOTE_AIRPORT_PROPERTIES = r"""
SELECT DISTINCT ?airport_code ?image ?inception
WHERE {{
    BIND("{code}" AS ?airport_code)
  
    ?airport wdt:P31/wdt:P279* wd:Q62447 ;
        wdt:P239 ?airport_code .
    OPTIONAL {{
        ?airport wdt:P18 ?image .
    }}
    OPTIONAL {{
        ?airport wdt:P571 ?inception .
    }}
}}
"""

LOCAL_AIRPORT_RUNWAYS = r"""
SELECT ?runway ?width ?length ?surface ?isLighted ?isClosed ?lowEndId WHERE {{
    BIND(:{code} as ?a)

    ?a verb:runway ?runway .
    ?runway verb:isLighted ?isLighted ;
    	verb:isClosed ?isClosed .
    
    OPTIONAL {{
        ?runway verb:width ?width .
    }}
    OPTIONAL {{
        ?runway verb:length ?length .
    }}
    OPTIONAL {{
        ?runway verb:surface ?surface .
    }}
    OPTIONAL {{
        ?runway verb:lowEndIdentifier ?lowEndId .
    }}
}}
"""

LOCAL_AIRPORT_NAVAIDS = r"""
SELECT ?airport ?name ?navAidType ?latitude ?longitude ?elevation ?frequency ?magnetic ?usageType ?power WHERE {{
    BIND(:{code} as ?airport)
    
    ?navaids verb:associatedAirport ?airport ;
    	rdfs:label ?name ;
    	verb:navAidType ?navAidType .
    
    OPTIONAL {{
        ?navaids verb:geographicLocation ?b1 .
        ?b1 verb:latitudeDegree ?latitude ;
        	verb:longitudeDegree ?longitude .
        OPTIONAL {{
            ?b1 verb:elevation ?elevation .
        }}
    }}
    OPTIONAL {{
        ?navaids verb:navigationUsage ?b2 .
        ?b2 verb:frequencyKhz ?frequency .
        OPTIONAL {{
            ?b2 verb:magneticVariation ?magnetic .
        }}
        OPTIONAL {{
            ?b2 verb:usageType ?usageType .
        }}
        OPTIONAL {{
            ?b2 verb:power ?power .
        }}
    }}
}}
"""