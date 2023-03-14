from SPARQLWrapper import SPARQLWrapper, JSON, XML, CSV
from constants import USER_NAME,PASSWORD


class Queryer():
    def __init__(self, endpoint, returnFormat = 'JSON'):

        supportedReturnFormats = {
            'JSON': JSON,
            'XML': XML,
            'CSV': CSV
        }

        self.sparql = SPARQLWrapper(endpoint)
        self.returnFormat = supportedReturnFormats[returnFormat.upper()]
    
    def request(self,query:str):
        '''
            Request data from sparql endpoint

            #### Parameters

            query: Sparql Query to execute 
        '''
        # Set global credentials
        self.sparql.setCredentials(USER_NAME,PASSWORD)
        self.sparql.setReturnFormat(self.returnFormat)

        # Set Query
        self.sparql.setQuery(query)

        # Try sending request
        try:
            response = self.sparql.queryAndConvert()["results"]["bindings"]

            #print("Next Entered")
            for dict_el in response:
                dict_copy = dict(dict_el)
                for val in dict_copy:
                    if dict_el[val]['type'] == "uri":
                        # Get Value of URI
                        dict_el[val]["type"] = "literal"
                        dict_el[val]["value"] = str(dict_el[val]["value"].split("/")[-1]).replace("_", " ")

            return response
        except Exception as e:
            print(e)

    
    def select_query(self, query):
        base_query = '''
            PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

            SELECT {DISTINCT} {VARS} WHERE {{
                {QUERY}
            }}
            {OPTIONS}
        '''

        # Set Credentials for endpoint and data return type
        self.sparql.setCredentials(USER_NAME,PASSWORD)
        self.sparql.setReturnFormat(self.returnFormat)

        # Set Query
        base_query = base_query.format(
            VARS = ' '.join(query['VARS']), 
            QUERY =query['QUERY'],
            DISTINCT = 'DISTINCT' if query['DISTINCT'] else '',
            OPTIONS = ' \n'.join(query['OPTIONS'])
            )

        self.sparql.setQuery(base_query)
        
        # Send response to endpoint
        try:
            response = self.sparql.queryAndConvert()["results"]["bindings"]


            for dict_el in response:
                dict_copy = dict(dict_el)
                for val in dict_copy:
                    if dict_el[val]['type'] == "uri":
                        # Get Value of URI
                        dict_el[val]["type"] = "literal"
                        dict_el[val]["value"] = str(dict_el[val]["value"].split("/")[-1]).replace("_"," ")
               
            return response

        except Exception as e:
            print(e)