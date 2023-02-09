from flask_restful import Resource
from flask import request
from Common.queryer import Queryer


class Cohort(Resource):

   def __init__(self, cohortName:str) -> None:
      super().__init__()

      # Initialize Class Variables
      self.cohortName = cohortName

   def get(self):
      pass

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
   
   # Get List of Cohorts part of a project
    def post(self):
      obj = Queryer(self.endpoint)
      
      project_name = request.get_json()['projectName']
        # <TODO> Get Project name from Args and pass data
      # project_name = "Proj ENIGMA3 Cortical GWAS"
    
      query = {
         "VARS": ['?cohortName'],
         "QUERY": self.base_query.format(projectName=project_name),
         "DISTINCT": False,
         "OPTIONS": ''
      }

      response = obj.select_query(query) 

      return response