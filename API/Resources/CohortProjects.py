from flask_restful import Resource
from flask import request

from Common.queryer import Queryer
from Common import QueryBuilder as QB
from flask_cors import CORS, cross_origin

# @cross_origin()
class CohortProject(Resource):
    def get(self, cohort_name, cohort_project_name):
        return cohort_name.replace("_"," ")

    def post(self, cohort_name, cohort_project_name):
        body = request.get_json()
        obj = Queryer(body['endpoint_id'])
        cohort_project_name=cohort_project_name.replace("_", " ")
        print(cohort_project_name)
        query = f'''
              ?project a ?projectClass.
            ?projectClass rdfs:label "{body['projType']}".
            
            ?projectName rdfs:label "{body['name']}" .
            
            ?project ?hasCohort ?cohort.
            ?hasCohort rdfs:label "HasCohort (E)".
  			?cohort rdfs:label ?cohortProjname .
  
  			?cohort ?hasCohortProj ?cohortprojects.
            ?hasCohortProj rdfs:label "HasCohortProject (E)".
  			?cohortprojects rdfs:label ?cohortProjectname .
  
            ?cohortprojects ?hasProp ?propsURI.
            ?hasProp rdfs:label ?props.
            
            filter(?cohortProjname = "{cohort_name}")
            filter(?cohortProjectname = "{cohort_project_name}")
        '''
        vars = ['?props','?propsURI']

        qb = QB.QueryBuilder()
        qb.set_query(query=query, vars=vars)

        response = obj.request(qb.get_query())

        return response

# @cross_origin()
class CohortProjectList(Resource):
    def get(self, cohort_name:str) -> str:
        return cohort_name.replace('_', ' ')
    
    def post(self, cohort_name: str):
        body = request.get_json()
        obj = Queryer(body['endpoint_id'])
        cohort_name = cohort_name.replace('_',' ')
        print(cohort_name)

        query = f'''
            ?cohort a ?cohortClass.
            ?cohortClass rdfs:label "Cohort (E)".
  
            ?cohort rdfs:label "{cohort_name}".
  
            ?cohort ?hasCohortProj ?cohortProj.
            ?hasCohortProj rdfs:label "HasCohortProject (E)".
  
            ?cohortProj rdfs:label ?cohortProjName.
        '''
        vars = ['?cohortProjName']

        qb = QB.QueryBuilder()
        qb.set_query(query=query, vars=vars)

        response = obj.request(qb.get_query())
        
        return response




