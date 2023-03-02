from flask_restful import Resource
from flask import request

from Common.queryer import Queryer
from Common import QueryBuilder as QB

class CohortProject(Resource):
    def get(self, cohort_project):
        return cohort_project.replace("_"," ")

    def post(self, cohort_name, cohort_project_name):
        body = request.get_json()
        obj = Queryer(body['endpoint_id'])

        query = '''
              ?cohort a ?cohortClass.
            ?cohortClass rdfs:label "Cohort (E)".
  
            ?cohort rdfs:label "CHRISTCHURCH".
  
            ?cohort ?hasCohortProj ?cohortProj.
            ?hasCohortProj rdfs:label "HasCohortProject (E)".
  
            ?cohortProj rdfs:label ?cohortProjName.
        '''
        vars = ['cohortProjName']

        qb = QB.QueryBuilder()
        qb.set_query(query=query, vars=vars)

        response = obj.select_query(qb.get_query())

        return response

class CohortProjectList(Resource):
    def get(self, cohort_name:str) -> str:
        return cohort_name.split('_', ' ')
    
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
    

        