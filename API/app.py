from flask import Flask
from flask_restful import Api

# Import Resources
from Resources.Cohorts import CohortList

app = Flask(__name__)
api = Api(app)

endpoint = "https://enigma-endpoint.disk.isi.edu/enigma_dev/sparql"

# Register All Resources Below

# Cohort URLS
api.add_resource(CohortList,
                 '/cohorts', 
                 resource_class_kwargs = {'endpoint':endpoint})

if __name__ == "__main__":
    app.run(debug=True)