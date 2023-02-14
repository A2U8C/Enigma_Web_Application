
baseQueries = {
    "working_group": """
        ?workingGroup a ?workingGroupClass.
        ?workingGroupClass rdfs:label "WorkingGroup (E)".
  
        ?workingGroupName rdfs:label "{name}".

    """,

    "project": """
        ?project a ?projectClass.
        ?projectClass rdfs:label "Project (E)".

        ?projectName rdfs:label "{name}" .

    """

}

def getBaseQuery(isWg):
    if isWg:
        return baseQueries["working_group"], '?workingGroup'
    else:
        return baseQueries["project"], '?project'

def formatQuery(vars:list, query:str , distinct:bool = False, options:list = []) -> str:
    query = {
        'VARS': vars,
        'QUERY': query,
        'DISTINCT': distinct,
        'OPTIONS' : options
    }

    return query