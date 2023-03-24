from flask_restful import Resource, abort
from flask import request

from Common.queryer import Queryer
from Common import QueryBuilder as QB

from .Cohorts import CohortList

from collections import defaultdict

from constants import missing_datasets

# Needs to be changed
dict_covar = {}
dict_covar["Has cognitive (E)"] = ['WordListLearningTask (E)', 'DigitSpanBackward (E)',
                                   'Rey_OsterriethComplexFigureTest (E)', 'SWCT (E)', 'SentencesConstruction (E)',
                                   'PhonologicalAndSemanticVerbalFluencyTest (E)', 'TrialMakingTestA-B (E)',
                                   'Reys15WordTest (E)', 'DigitSpanForward (E)', 'MoCA (E)', 'MMSE (E)',
                                   'OtherCognitiveCovariates (E)', 'WCST-SF (E)', 'PD_DementiaDiagnosis (E)',
                                   'MildCognitiveImpairmentDiagnosis (E)', 'Name (E)']
dict_covar["Has PD Demographics (E)"] = ['MDS-UPDRSTotal (E)', 'CityDwelling (E)', 'SCOPA-Sleep (E)', 'SubjectSES (E)',
                                         'SCOPA-Cognition (E)', 'OtherMotorEvaluation (E)', 'Iq (E)', 'UPDRSTotal (E)',
                                         'Sex (E)', 'SideOfOnset (E)', 'OtherMedUseLifetime (E)', 'MDS-UPDRS-3 (E)',
                                         'MDS-UPDRS-2 (E)', 'MDS-UPDRS-1 (E)', 'Comorbidities (E)', 'UPSIT (E)',
                                         'Age (E)', 'PDMedicationUseLifetime (E)', 'MDS-UPDRS-4 (E)',
                                         'HoehnAndYahrStage (E)', 'RBDDiagnosis (E)', 'UPDRS-1 (E)', 'UPDRS-2 (E)',
                                         'RaceEthnicity (E)', 'Handedness (E)', 'UPDRS-3 (E)', 'SCOPA-Autonomic (E)',
                                         'SCOPA-Motor (E)', 'Education (E)', 'PatientMedicationOnOffDuringUPDRS (E)',
                                         'Durill (E)', 'OtherDemographics (E)', 'UPDRS-4 (E)', 'MaritalStatus (E)',
                                         'PDMotorSubtype (E)', 'SubjID (E)', 'DiagnosisConfirmed (E)', 'SE-ADLS (E)',
                                         'OtherPDDiagnosisData (E)', 'Occupation (E)', 'OtherEnvironmentalFactors (E)',
                                         'SCOPA-Psychiatric (E)', 'RSGE-PD (E)', 'AgeOfPDOnset (E)', 'Dx (E)',
                                         'LEDDScore (E)', 'PDMedicationUseCurrent (E)', 'OtherMedUseCurrent (E)',
                                         'Name (E)']
dict_covar["Has neuropsychiatric (E)"] = ['SASDQ (E)', 'RBD1Q (E)', 'RBDSQ (E)', 'STAXI (E)', 'BAI (E)', 'TAS-20 (E)',
                                          'IDS (E)', 'ISI (E)', 'ESS (E)', 'WOQ (E)', 'GDI (E)', 'UM-PDHQ (E)',
                                          'QPE (E)', 'PANNS (E)', 'KSS (E)', 'HAMA (E)', 'STAI (E)',
                                          'OtherNeuropsychiatricCovariates (E)', 'SHAPS (E)', 'AES (E)', 'BDI (E)',
                                          'PSQI (E)', 'MADRS (E)', 'PAS (E)', 'PDSS (E)', 'SAPS-PD (E)', 'QUIP-rs (E)',
                                          'AS (E)', 'HRDS (E)', 'PPRS (E)', 'Name (E)']


class CovariatePropertyList(Resource):
    def get(self, covariate_name):
        abort(403, message="Forbidden Method")

    def post(self, covariate_name):
        covariate_name = covariate_name.replace("_", " ")
        return dict_covar[covariate_name] if covariate_name in dict_covar.keys() else {}


# Needs to be changed
all_covariates = {"Cognitive": "Has cognitive (E)", "Demographic": "Has PD Demographics (E)",
                  "Neuro Psychiatric": "Has neuropsychiatric (E)"}


class all_CovariatesList(Resource):
    def get(self):
        abort(403, message="Forbidden Method")

    def post(self):
        return all_covariates


class CovariateCohortList(Resource):
    def get(self, covariate_name, covariate_prop_name):
        abort(403, message="Forbidden Method")

    def post(self, covariate_name, covariate_prop_name):
        body = request.get_json()
        obj = Queryer(body['endpoint_id'])

        covariate_name = covariate_name.replace("_", " ")
        covariate_prop_name = covariate_prop_name.replace("_", " ")


        query = f'''
            ?project a ?projectClass.
            ?projectClass rdfs:label "{body['projType']}".

            ?projectName rdfs:label "{body['name']}" . 
            ?project ?hasCohort ?cohortURI.
            #?hasCohort rdfs:label "HasCohort (E)".

  			?cohortURI ?propName ?ProjNameURI . 
  			?propName rdfs:label "{covariate_name}".

  			?ProjNameURI ?propCogName ?propProperty .
  			?propCogName rdfs:label "{covariate_prop_name}" .
  			
  			filter(?propProperty != false && ?propProperty != "FALSE") .

  			?cohortURI rdfs:label ?cohortName .

        '''

        vars = ['?cohortName']

        qb = QB.QueryBuilder()
        qb.set_query(query=query, vars=vars)

        response = obj.request(qb.get_query())

        print(qb.get_query())

        # dict_cohort_part={}
        # all_cohorts=CohortList().post()
        # all_cohorts=[i["cohortName"]["value"] for i in all_cohorts]
        # givenpresent=[i["cohortName"]["value"] for i in response]
        # givenabsent=list(set(all_cohorts)-missing_datasets-set(givenpresent))
        # dict_cohort_part["GivenPresent"]=givenpresent
        # dict_cohort_part["GivenAbsent"]=givenabsent
        # dict_cohort_part["Missing"]=list(missing_datasets)

        dict_cohort_part = {}
        cohortList_post = CohortList().post()
        all_cohorts = cohortList_post["presentCohorts"] + cohortList_post["Missing"]
        # print(all_cohorts)
        dict_cohort_part["all_cohorts"] = list(all_cohorts)

        givenpresent = [i["cohortName"]["value"] for i in response]
        givenabsent = list(set(all_cohorts) - missing_datasets - set(givenpresent))
        dict_cohort_part["GivenPresent"] = givenpresent
        dict_cohort_part["GivenAbsent"] = givenabsent
        dict_cohort_part["Missing"] = list(missing_datasets)

        return dict_cohort_part



class CovariateIntersectionCohorts(Resource):
    def get(self):
        abort(403, message="Forbidden Method")

    def post(self):
        body = request.get_json()
        cohort_dict=eval(body["data_covCoh"])
        obj = Queryer(body['endpoint_id'])

        f_val=""
        if cohort_dict=={}:
            return []

        for i in cohort_dict.keys():
            val=""
            # if i=="Has neuropsychiatric (E)":
            cov_label=i.split(" ")[1]+"Name"
            cov_uri="has"+i.split(" ")[1]+"URI"
            cov_prop=i.split(" ")[1]+"Prop"

            val +=f'''
                
                ?cohortURI ?{cov_label} ?{cov_uri} .
                ?{cov_label} rdfs:label "{i}".
                '''

            mid_el=i.split(" ")[1]+"_URI"
            for ind,j in enumerate(cohort_dict[i]):
                val+=f'''
                ?{cov_uri} ?{cov_prop}_{str(ind)} ?{mid_el} . 
                ?{cov_prop}_{str(ind)} rdfs:label "{j}" .
                '''
            val+=f'''
                filter(?{mid_el} = true) .
                '''

            f_val+=val


        query = f'''
                    ?project a ?projectClass.
                    ?projectClass rdfs:label "{body['projType']}".
        
                    ?projectName rdfs:label "{body['name']}" . 
                    ?project ?hasCohort ?cohortURI.
                    
                    ?cohortURI rdfs:label ?cohortName .'''+f_val

        vars = ['?cohortName']

        qb = QB.QueryBuilder()
        qb.set_query(query=query, vars=vars)

        print(qb.get_query())

        response = obj.request(qb.get_query())

        dict_cohort_part = {}
        array_coh=[i["cohortName"]["value"] for i in response]
        dict_cohort_part["all_present"] = array_coh




        return array_coh


        #return []


