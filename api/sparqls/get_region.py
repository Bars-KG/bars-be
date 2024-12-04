LOCAL_REGION_PROPERTIES = r"""
SELECT ?region ?regionName ?localCode ?country ?countryName
WHERE {{
    BIND(:{code} AS ?region)
    
   	?region rdfs:label ?regionName ;
    	verb:localCode ?localCode ;
    	verb:isoCountryCode ?country .
    ?country rdfs:label ?countryName .
}}
"""

REMOTE_REGION_PROPERTIES = r"""
SELECT DISTINCT ?region ?regionCode ?capitalName ?area ?population ?flagImage
WHERE {{
    BIND("{code}" AS ?regionCode)
  
    ?region wdt:P300 ?regionCode .
  OPTIONAL {{
    ?region wdt:P36 ?capital .
    ?capital rdfs:label ?capitalName .
    
    FILTER(LANG(?capitalName) = "en")
  }}
  OPTIONAL {{
    ?region wdt:P2046 ?area .
  }}
  OPTIONAL {{
    ?region wdt:P1082 ?population .
  }}
  OPTIONAL {{
    ?region wdt:P163 ?flag .
    ?flag wdt:P18 ?flagImage .
  }}
}}
LIMIT 1
"""