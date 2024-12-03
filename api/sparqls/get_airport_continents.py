LOCAL_GET_AIRPORT_CONTINENT_CODES = r"""
SELECT DISTINCT ?continent_codes WHERE {{
    ?airport rdf:type :Aerodrome;
    	verb:geographicLocation ?geographic_location.
    
    ?geographic_location verb:continentCode ?continent_codes .
}}
"""
