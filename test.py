from flask import Flask
from flask_restful import Api, Resource

from SPARQL_SERVER import queryer

app = Flask(__name__)
api = Api(app)

endpoint = "https://enigma-endpoint.disk.isi.edu/enigma_dev/sparql"

class Cohort(Resource):
   def get(self):
      pass

class CohortList(Resource):
    def __init__(self) -> None:
       
       super().__init__()
       # Initialize Base Query
       
       self.base_query = '''
            ?project a ?projectClass.
            ?projectClass rdfs:label "Project (E)".

            ?projectName rdfs:label "{projectName}" .

            ?project ?hasCohort ?cohort.
            ?hasCohort rdfs:label "HasCohort (E)".
  
            ?cohort rdfs:label ?cohortName.
       '''
   
   # Get List of Cohorts part of a project
    def get(self):
      obj = queryer.Queryer(endpoint)
        
        # <TODO> Get Project name from Args and pass data
      project_name = "Proj ENIGMA3 Cortical GWAS"
    
      query = {
         "VARS": ['?cohortName'],
         "QUERY": self.base_query.format(projectName=project_name)
      }

      response = obj.select_query(query) 

      return response

api.add_resource(CohortList, '/project')
api.add_resource(Cohort, '/project/<project_name>/<cohort_name>')

if __name__ == '__main__':
    app.run(debug=True)