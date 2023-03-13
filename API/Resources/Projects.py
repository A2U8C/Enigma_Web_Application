from flask_restful import Resource, abort
from flask import request

from Common.queryer import Queryer
from Common import QueryBuilder as QB
from collections import defaultdict
from .Cohorts import CohortList

class ProjectList(Resource):
    def get(self):
        abort(403, message="Forbidden Method")

    def post(self):
        body = request.get_json()
        obj = Queryer(body['endpoint_id'])

        query = f'''
            ?project a ?projectClass.
            ?projectClass rdfs:label "{body['projType']}".

            #?projectName rdfs:label "{body['name']}" .

            ?project ?hasCohort ?cohortURI.
            ?hasCohort rdfs:label "HasCohort (E)".
  
  			?cohortURI ?propName ?ProjNameURI . 
  			?propName rdfs:label "IsPartOfProject (E)" .
  
  			?cohortURI rdfs:label ?cohort .
  			?ProjNameURI rdfs:label ?ProjName .
        '''

        vars = ['?cohort','?ProjName']

        qb = QB.QueryBuilder()
        qb.set_query(query=query, vars=vars)

        response = obj.request(qb.get_query())

        print(type(response))

        all_know_cohorts=set(CohortList().post()["presentCohorts"]+CohortList().post()["Missing"])


        dict_proj_name=defaultdict(list)

        all_list=set()
        for i in response:
            dict_proj_name[i["ProjName"]["value"]].append(i["cohort"]["value"])

            dict_proj_name[i["ProjName"]["value"]]=sorted(dict_proj_name[i["ProjName"]["value"]])
            all_list.add(i["cohort"]["value"])

        dict_proj_name["Unknown"]=sorted(all_know_cohorts-all_list)
        # dict_proj_name["allCohorts"]=list(all_list)
        return dict_proj_name