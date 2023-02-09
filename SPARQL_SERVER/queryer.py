from SPARQLWrapper import SPARQLWrapper, JSON, XML
from constants import USER_NAME,PASSWORD

class Queryer():
    def __init__(self, endpoint, returnFormat = 'json'):
        self.sparql = SPARQLWrapper(endpoint)
        self.returnFormat = returnFormat
        
    
    def select_query(self, query):
        base_query = '''
            PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

            SELECT {VARS} WHERE {{
                {QUERY}
            }}
            LIMIT 10
        '''

        # Set Credentials for endpoint and data return type
        self.sparql.setCredentials(USER_NAME,PASSWORD)

        if self.returnFormat == 'json':
            self.sparql.setReturnFormat(JSON)
        elif self.returnFormat == 'xml':
            self.sparql.setReturnFormat(XML)
        
        # Set Query
        base_query = base_query.format(VARS = ' '.join(query['VARS']), QUERY =query['QUERY'] )
        self.sparql.setQuery(base_query)
        
        # Send response to endpoint
        try:
            response = self.sparql.queryAndConvert()
            return response["results"]["bindings"]

        except Exception as e:
            print(e)


            



