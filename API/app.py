from flask import Flask
from flask_restful import Api

# Import Resources
from Resources.Cohorts import CohortList, Cohort
from Resources.CohortProjects import CohortProject

app = Flask(__name__)
api = Api(app)

# Register All Resources Below

# Cohort URLS
api.add_resource(CohortList,'/cohorts')
api.add_resource(Cohort,'/cohort/<string:cohort_name>')
api.add_resource(CohortProject, '/cohort/project/<string:cohort_project>')

if __name__ == "__main__":
    app.run(debug=True)