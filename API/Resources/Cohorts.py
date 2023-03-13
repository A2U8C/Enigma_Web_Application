from flask_restful import Resource, abort
from flask import request

from Common.queryer import Queryer
from Common import QueryBuilder as QB
# from Common.utils import formatQuery
from flask_cors import CORS, cross_origin
from constants import missing_datasets

from collections import OrderedDict

# Get the property values of cohort
# @cross_origin()
class Cohort(Resource):
    def get(self, cohort_name: str) -> str:
        return cohort_name.replace('_', ' ')

    def post(self, cohort_name: str):
        print(cohort_name)
        body = request.get_json()
        obj = Queryer(body['endpoint_id'])
        cohort_name = cohort_name.replace('_', ' ')

        query = f'''
            ?project a ?projectClass.
            ?projectClass rdfs:label "{body['projType']}".

            ?projectName rdfs:label "{body['name']}" .

            ?project ?hasCohort ?cohort.
            ?hasCohort rdfs:label "HasCohort (E)".

            ?cohort rdfs:label ?cohortName.
            ?cohort ?hasProp ?propsURI.
            ?hasProp rdfs:label ?props.

            ?cohort ?cohortprop ?propsval .
            ?cohortprop rdfs:label ?props .
            #IF(?propsval_uri rdfs:label ?propsval, ?propsval, ?props) .

            filter(?cohortName = "{cohort_name}")
        '''
        vars = ['?props','?propsval']

        qb = QB.QueryBuilder()
        qb.set_query(query=query, vars=vars)

        response = obj.request(qb.get_query())

        return response
# Get List of Cohorts part of a project or Working Group

# @cross_origin()
class CohortList(Resource):
    def get(self):
       abort(403,message="Forbidden Method")

    def post(self):
        body = request.get_json()
        obj = Queryer(body['endpoint_id'])


        query = f'''
            ?project a ?projectClass.
            ?projectClass rdfs:label "{body['projType']}".

            ?project rdfs:label "{body['name']}".

            ?project ?hasCohort ?cohort.
            ?hasCohort rdfs:label "HasCohort (E)".
  
            ?cohort rdfs:label ?cohortName .
        '''
        
        vars = ['?cohortName']

        qb = QB.QueryBuilder()
        qb.set_query(query=query, vars=vars)
        #,modifiers={"Order by" : "ASC(?cohortName)"}
       
        response = obj.request(qb.get_query())

        dict_cohort_part = {}
        all_cohorts = [i["cohortName"]["value"] for i in response]
        present_cohorts = sorted(set(all_cohorts) - missing_datasets)
        dict_cohort_part["presentCohorts"] = present_cohorts
        dict_cohort_part["Missing"] = sorted(missing_datasets)


        print("***************************************************************",dict_cohort_part)
        return dict_cohort_part
        # return response


# @cross_origin()
class CohortDetails(Resource):
    def get(self, cohort_name: str) -> str:
        return cohort_name.replace('_', ' ')

    def post(self, cohort_name: str):
        print(cohort_name)
        body = request.get_json()
        obj = Queryer(body['endpoint_id'])
        cohort_name = cohort_name.replace('_', ' ')

        query = f'''
            ?project a ?projectClass.
            ?projectClass rdfs:label "{body['projType']}".
            
            ?projectName rdfs:label "{body['name']}" . 

            ?project ?hasCohort ?cohortURI.
            ?hasCohort rdfs:label "HasCohort (E)".
 
  			?cohortURI ?propURI ?PropValURI.
  			?propURI rdfs:label ?prop .
  			#?PropValURI rdfs:label ?propvalue .
  
  
  			?cohortURI rdfs:label ?cohort .
  			filter(?cohort = "{cohort_name}")
        '''
        vars = ['?prop','?PropValURI']

        qb = QB.QueryBuilder()
        qb.set_query(query=query, vars=vars)

        response = obj.request(qb.get_query())

        return response

