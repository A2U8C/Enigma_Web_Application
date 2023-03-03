from flask import Flask
from flask_restful import Api

# Import Resources
from Resources.Cohorts import CohortList, Cohort
from Resources.CohortProjects import CohortProject, CohortProjectList

app = Flask(__name__)
api = Api(app)

# Register All Resources Below

# Cohort URLS
api.add_resource(CohortList,'/cohorts') #Done
api.add_resource(CohortProjectList, '/cohorts/<string:cohort_name>/projects')#Done


api.add_resource(Cohort,'/cohorts/<string:cohort_name>') #Done
api.add_resource(CohortProject, '/cohorts/<string:cohort_name>/projects/<string:cohort_project_name>')#Done

if __name__ == "__main__":
    app.run(debug=True)