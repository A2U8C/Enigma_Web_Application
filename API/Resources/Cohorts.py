from flask_restful import Resource, abort
from flask import request

from Common.queryer import Queryer
from Common import QueryBuilder as QB
# from Common.utils import formatQuery


# Get the property values of cohort
class Cohort(Resource):

    def get(self,cohort_name):
        return cohort_name.replace("_", " ")

    def post(self,cohort_name):
        
        body = request.get_json()
        obj = Queryer(body['endpoint_id'])
        query,vars = QB.getCohortNameQuery(cohort_name.replace("_"," ")) 
        
        query = formatQuery(vars, query, distinct=True)
       
        response = obj.select_query(query)
        return response

# Get List of Cohorts part of a project or Working Group
class CohortList(Resource):
    def get(self):
       abort(403,message="Forbidden Method")

    def post(self):
        body = request.get_json()
        obj = Queryer(body['endpoint_id'])


        query = f'''
            ?project a ?projectClass.
            ?projectClass rdfs:label "Project (E)".

            ?project rdfs:label "{body['name']}".

            ?project ?hasCohort ?cohort.
            ?hasCohort rdfs:label "HasCohort (E)".
  
            ?cohort rdfs:label ?cohortName .
        '''
        
        vars = ['?cohortName']

        qb = QB.QueryBuilder()
        qb.set_query(query=query, vars=vars)
        
        response = obj.request(qb.get_query())
        return response