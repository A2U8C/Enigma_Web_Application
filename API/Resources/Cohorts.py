from flask_restful import Resource
from flask import request
from Common.queryer import Queryer


class Cohort(Resource):

      # Initialize Class Variables
      #self.cohortName = cohortName
    def __init__(self, **kwargs) -> None:
        super().__init__()

        # Initialize class variables
        self.base_query = '''
            ?project a ?projectClass.
            ?projectClass rdfs:label "Project (E)".
            
            ?projectName rdfs:label "{projectName}" .
            
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
        
        self.endpoint = kwargs['endpoint']

    def get(self,cohort_name):
        return "Helllo"

       # Get List of Cohorts part of a project

    def post(self,cohort_name):
        # print(cohort_name+"***************************************")
        obj = Queryer(self.endpoint)

        project_name = request.get_json()['projectName']

        query = {
           "VARS": ['?props','?propsval'],
           "QUERY": self.base_query.format(projectName=project_name,cohort_name=cohort_name),
           "DISTINCT": False,
           "OPTIONS": ''
        }

        response = obj.select_query(query)
        return response

class CohortList(Resource):
    def __init__(self, **kwargs) -> None:
       
       super().__init__()

       # Initialize class variables
       self.base_query = '''
            ?project a ?projectClass.
            ?projectClass rdfs:label "Project (E)".

            ?projectName rdfs:label "{projectName}" .

            ?project ?hasCohort ?cohort.
            ?hasCohort rdfs:label "HasCohort (E)".
  
            ?cohort rdfs:label ?cohortName.
       '''
       self.endpoint = kwargs['endpoint']

    def get(self):
       return "Helllo"

   # Get List of Cohorts part of a project
    def post(self):
      obj = Queryer(self.endpoint)

      project_name = request.get_json()['projectName']

      query = {
         "VARS": ['?cohortName'],
         "QUERY": self.base_query.format(projectName=project_name),
         "DISTINCT": False,
         "OPTIONS": ''
      }

      response = obj.select_query(query)
      return response