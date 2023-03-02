from flask import Flask
from flask_restful import Api

# Import Resources
from Resources.Cohorts import CohortList, Cohort
from Resources.CohortProjects import CohortProject, CohortProjectList

app = Flask(__name__)
api = Api(app)

# Register All Resources Below

# Cohort URLS
api.add_resource(CohortList,'/cohort')
api.add_resource(Cohort,'/cohort/<string:cohort_name>')
api.add_resource(CohortProject, '/cohort/<string:cohort_name>/project/<string:cohort_project>')
api.add_resource(CohortProjectList, '/cohort/<string:cohort_name>/project')

if __name__ == "__main__":
    app.run(debug=True)