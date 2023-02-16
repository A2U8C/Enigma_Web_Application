def URIToValue(URI):
    query = f"""
        SELECT ?val {{
            {URI} rdfs:label ?val.
        }}
    """
    return query

def formatQuery(vars:list, query:str , distinct:bool = False, options:list = []) -> str:
    query = {
        'VARS': vars,
        'QUERY': query,
        'DISTINCT': distinct,
        'OPTIONS' : options
    }

    return query
