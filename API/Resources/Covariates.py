from flask_restful import Resource, abort
from flask import request

from Common.queryer import Queryer
from Common import QueryBuilder as QB
from collections import defaultdict


#Needs to be changed

dict_covar = {}

dict_covar["Has cognitive (E)"] = ['WordListLearningTask (E)', 'DigitSpanBackward (E)', 'Rey_OsterriethComplexFigureTest (E)', 'SWCT (E)', 'SentencesConstruction (E)', 'PhonologicalAndSemanticVerbalFluencyTest (E)', 'TrialMakingTestA-B (E)', 'Reys15WordTest (E)', 'DigitSpanForward (E)', 'MoCA (E)', 'MMSE (E)', 'OtherCognitiveCovariates (E)', 'WCST-SF (E)', 'PD_DementiaDiagnosis (E)', 'MildCognitiveImpairmentDiagnosis (E)', 'Name (E)']

dict_covar["Has PD Demographics (E)"] = ['MDS-UPDRSTotal (E)', 'CityDwelling (E)', 'SCOPA-Sleep (E)', 'SubjectSES (E)', 'SCOPA-Cognition (E)','OtherMotorEvaluation (E)', 'Iq (E)', 'UPDRSTotal (E)', 'Sex (E)', 'SideOfOnset (E)', 'OtherMedUseLifetime (E)', 'MDS-UPDRS-3 (E)', 'MDS-UPDRS-2 (E)', 'MDS-UPDRS-1 (E)', 'Comorbidities (E)', 'UPSIT (E)', 'Age (E)', 'PDMedicationUseLifetime (E)', 'MDS-UPDRS-4 (E)', 'HoehnAndYahrStage (E)', 'RBDDiagnosis (E)', 'UPDRS-1 (E)', 'UPDRS-2 (E)', 'RaceEthnicity (E)', 'Handedness (E)', 'UPDRS-3 (E)', 'SCOPA-Autonomic (E)', 'SCOPA-Motor (E)', 'Education (E)', 'PatientMedicationOnOffDuringUPDRS (E)', 'Durill (E)', 'OtherDemographics (E)', 'UPDRS-4 (E)', 'MaritalStatus (E)', 'PDMotorSubtype (E)', 'SubjID (E)', 'DiagnosisConfirmed (E)', 'SE-ADLS (E)', 'OtherPDDiagnosisData (E)', 'Occupation (E)', 'OtherEnvironmentalFactors (E)', 'SCOPA-Psychiatric (E)', 'RSGE-PD (E)', 'AgeOfPDOnset (E)', 'Dx (E)', 'LEDDScore (E)', 'PDMedicationUseCurrent (E)', 'OtherMedUseCurrent (E)', 'Name (E)']

dict_covar["Has neuropsychiatric (E)"] = ['SASDQ (E)', 'RBD1Q (E)', 'RBDSQ (E)', 'STAXI (E)', 'BAI (E)', 'TAS-20 (E)', 'IDS (E)', 'ISI (E)', 'ESS (E)', 'WOQ (E)', 'GDI (E)', 'UM-PDHQ (E)', 'QPE (E)', 'PANNS (E)', 'KSS (E)', 'HAMA (E)', 'STAI (E)', 'OtherNeuropsychiatricCovariates (E)', 'SHAPS (E)', 'AES (E)', 'BDI (E)', 'PSQI (E)', 'MADRS (E)', 'PAS (E)', 'PDSS (E)', 'SAPS-PD (E)', 'QUIP-rs (E)', 'AS (E)', 'HRDS (E)', 'PPRS (E)', 'Name (E)']

class CovariatesList(Resource):
    def get(self, covariate_name):
        abort(403, message="Forbidden Method")

    def post(self, covariate_name):

        covariate_name = covariate_name.replace("_", " ")



        return dict_covar[covariate_name] if covariate_name in dict_covar.keys() else {}



class CovariateProperty(Resource):
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

            #?projectName rdfs:label "{body['projType']}" .

            ?project ?hasCohort ?cohortURI.
            ?hasCohort rdfs:label "HasCohort (E)".
  
  			?cohortURI ?propName ?ProjNameURI . 
  			?propName rdfs:label "{covariate_name}".
  
  			?ProjNameURI ?propCogName ?propProperty .
  			?propCogName rdfs:label "{covariate_prop_name}" .
  
  			?cohortURI rdfs:label ?cohortName .
        
        '''

        vars = ['?cohortName']

        qb = QB.QueryBuilder()
        qb.set_query(query=query, vars=vars)

        response = obj.request(qb.get_query())

        print(type(response))

        return response