from flask import Flask
from flask_restful import Api

# Import Resources
from Resources.Cohorts import CohortList
from Resources.Cohorts import Cohort

app = Flask(__name__)
api = Api(app)

# Register All Resources Below

# Cohort URLS
api.add_resource(CohortList,'/cohorts')

api.add_resource(Cohort,'/cohort/<string:cohort_name>')


if __name__ == "__main__":
    app.run(debug=True)