def getProjectNameQuery(project_name):

    query = f"""
        ?name a ?projectClass.
        ?projectClass rdfs:label "Project (E)".

        ?name rdfs:label "{project_name}" .
    """
    return query, ["?name"]

def getWorkingGroupNameQuery(working_group_name):

    query = f"""
         ?name a ?workingGroupClass.
        ?workingGroupClass rdfs:label "WorkingGroup (E)".
  
        ?name rdfs:label "{working_group_name}".
    """
    
    return query, ["?name"]

def getCohortNameListQuery():
    query = """
        ?name ?hasCohort ?cohort.
        ?hasCohort rdfs:label "HasCohort (E)".
  
        ?cohort rdfs:label ?cohortName.
    """
    return query,["?cohortName"]

def getCohortNameQuery(cohort_name:str):

    vars = ["?propsVal","?props"]
    
    query = f"""
            ?name ?hasCohort ?cohort.
            ?hasCohort rdfs:label "HasCohort (E)".
            
            ?cohort rdfs:label ?cohortName.
            ?cohort ?hasProp ?propsURI.
            ?hasProp rdfs:label ?props.
            
            ?cohort ?cohortprop {vars[0]} .
            ?cohortprop rdfs:label {vars[1]} .
            
            filter(?cohortName = "{cohort_name}").
    """
    return query,vars

def getCohortProjectQuery(cohort_project_name):
    vars = ["?propsVal", "?props"]
    query =f"""
            ?name ?hasCohortProj ?cohortProj.
            ?hasCohortProj rdfs:label "HasCohortProject (E)".
            
            ?cohortProj rdfs:label ?cohortProjName.
            ?cohortProj ?hasProp ?propsURI.
            ?hasProp rdfs:label ?props.
            
            ?cohortProj ?cohortProjProp {vars[0]} .
            ?cohortProjProp rdfs:label {vars[1]} .
            
            filter(?cohortProjName = "{cohort_project_name}").
    """

    return query,vars