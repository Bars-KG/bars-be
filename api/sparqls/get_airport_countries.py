LOCAL_GET_AIRPORT_COUNTRIES = r"""
SELECT ?country ?name WHERE {{
    ?country a :country ;
    	rdfs:label ?name ;
    	verb:continentCode :{continent_code} .
}}
ORDER BY ?name
"""

