LOCAL_COUNTRY_PROPERTIES = r"""
SELECT
?country ?countryName ?continent ?population ?density ?area ?gdp ?agriculture ?industry ?service ?netMigration ?infantMortality ?birthrate ?deathrate ?arableLand ?cropsLand ?otherLand ?literacy ?phoneDensity ?coastline
WHERE {{
    BIND(:{code} AS ?country)
    BIND(IRI(CONCAT("http://data.bars-kg.com/entity/", ?countrySafeName)) AS ?countryFull)
    
    ?country rdf:type :country ;
    	rdfs:label ?countryName ;
        verb:continentCode ?continent ;
    	verb:safeName ?countrySafeName .
    
    ?countryFull verb:coastline ?coastline .
    
    OPTIONAL {{
        ?countryFull verb:demographic ?b1 .
        ?b1 verb:population ?population ;
        	verb:area ?area ;
        	verb:populationDensity ?density .
    }}
    OPTIONAL {{
        ?countryFull verb:economy ?b2 .
        ?b2 verb:gdp ?gdp .
        
        OPTIONAL {{
            ?b2 verb:agriculture ?agriculture .
        }}
        OPTIONAL {{
            ?b2 verb:industry ?industry .
        }}
        OPTIONAL {{
            ?b2 verb:service ?service .
        }}
    }}
    OPTIONAL {{
        ?countryFull verb:healthQuality ?b3 .
        
        OPTIONAL {{
            ?b3 verb:netMigration ?netMigration .
        }}
        OPTIONAL {{
            ?b3 verb:infantMortality ?infantMortality .
        }}
        OPTIONAL {{
            ?b3 verb:birthrate ?birthrate .
        }}
        OPTIONAL {{
            ?b3 verb:deathrate ?deathrate .
        }}
    }}
    OPTIONAL {{
        ?countryFull verb:landUsage ?b4 .
        
        OPTIONAL {{
            ?b4 verb:arable ?arableLand .
        }}
        OPTIONAL {{
            ?b4 verb:crops ?cropsLand .
        }}
        OPTIONAL {{
            ?b4 verb:otherLandUse ?otherLand .
        }}
    }}
    OPTIONAL {{
        ?countryFull verb:literacy ?literacy .
    }}
    OPTIONAL {{
        ?countryFull verb:phoneDensity ?phoneDensity .
    }}
}}
"""

REMOTE_COUNTRY_PROPERTIES = r"""
SELECT DISTINCT ?countryCode ?capitalName ?headOfStateName ?flagImage ?currencyName ?inception
WHERE {{
    BIND("{code}" AS ?countryCode)
  
    ?country wdt:P31/wdt:P279* wd:Q6256 ;
        wdt:P297 ?countryCode .
  OPTIONAL {{
    ?country wdt:P36 ?capital .
    ?capital rdfs:label ?capitalName .
    
    FILTER(LANG(?capitalName) = "en")
  }}
  OPTIONAL {{
    ?country wdt:P35 ?headOfState .
    ?headOfState rdfs:label ?headOfStateName .
    
    FILTER(LANG(?headOfStateName) = "en")
  }}
  OPTIONAL {{
    ?country wdt:P163 ?flag .
    ?flag wdt:P18 ?flagImage .
  }}
  OPTIONAL {{
    ?country wdt:P38 ?currency .
    ?currency rdfs:label ?currencyName .
    
    FILTER(LANG(?currencyName) = "en")
  }}
  OPTIONAL {{
    ?country wdt:P571 ?inception .
  }}
}}
LIMIT 1
"""