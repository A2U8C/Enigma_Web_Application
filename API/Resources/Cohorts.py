from flask_restful import Resource
from flask import request
from Common.queryer import Queryer
from Common.QueryBuilder import formatQuery, getBaseQuery


class Cohort(Resource):

    def get(self,cohort_name):
        return cohort_name

       # Get List of Cohorts part of a project

    def post(self,cohort_name):
        # print(cohort_name+"***************************************")
        body = request.get_json()
        obj = Queryer(body['endpoint_id'])

        base_query, access_variable = getBaseQuery(body['isWG'])
        base_query = base_query.format(name = body['name'])

        query = f'''
            {access_variable} ?hasCohort ?cohort.
            ?hasCohort rdfs:label "HasCohort (E)".
            
            ?cohort rdfs:label ?cohortName.
            ?cohort ?hasProp ?propsURI.
            ?hasProp rdfs:label ?props.
            
            ?cohort ?cohortprop ?propsval .
            ?cohortprop rdfs:label ?props .
            
            filter(?cohortName = "{cohort_name}")
        '''

        query = formatQuery(['?props','?propsval'], base_query + query)

        response = obj.select_query(query)
        return response

class CohortList(Resource):
    def get(self):
       return "Helllo"

   # Get List of Cohorts part of a project
    def post(self):
      body = request.get_json()
      obj = Queryer(body['endpoint_id'])

      base_query, access_variable = getBaseQuery(body['isWG'])
      base_query = base_query.format(name = body['name'])

      query = f'''
        {access_variable} ?hasCohort ?cohort.
        ?hasCohort rdfs:label "HasCohort (E)".
  
        ?cohort rdfs:label ?cohortName.
      '''
      
      query = formatQuery(['?cohortName'],base_query + query)
      response = obj.select_query(query)
      
      return response