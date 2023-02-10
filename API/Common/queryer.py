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

            SELECT {DISTINCT} {VARS} WHERE {{
                {QUERY}
            }}
            {OPTIONS}
        '''

        # Set Credentials for endpoint and data return type
        self.sparql.setCredentials(USER_NAME,PASSWORD)

        if self.returnFormat == 'json':
            self.sparql.setReturnFormat(JSON)
        elif self.returnFormat == 'xml':
            self.sparql.setReturnFormat(XML)
        
        # Set Query
        base_query = base_query.format(
            VARS = ' '.join(query['VARS']), 
            QUERY =query['QUERY'],
            DISTINCT = 'DISTINCT' if query['DISTINCT'] else '',
            OPTIONS = ' \n'.join(query['OPTIONS'])
            )

        print("Queryer")
        self.sparql.setQuery(base_query)
        
        # Send response to endpoint
        try:
            response = self.sparql.queryAndConvert()["results"]["bindings"]
            for dict_el in response:
                if dict_el["propsval"]["type"]=="uri":
                    dict_el["propsval"]["type"] = "literal"
                    dict_el["propsval"]["value"] = str(dict_el["propsval"]["value"].split("/")[-1]).replace("_"," ")

            return response

        except Exception as e:
            print(e)


            



