from flask_restful import Resource
from flask import request

from Common.queryer import Queryer
from Common import QueryBuilder as QB
from Common.utils import formatQuery

class CohortProject(Resource):
    def get(self, cohort_project):
        return cohort_project.replace("_"," ")

    def post(self, cohort_project):
        body = request.get_json()
        obj = Queryer(body['endpoint_id'])

        query,vars = QB.getCohortProjectQuery(cohort_project.replace('_', " "))
        query = formatQuery(vars, query,distinct=True)
        
        response = obj.select_query(query)

        return response

class CohortProjectList(Resource):
    pass

        