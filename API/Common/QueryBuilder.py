from Common.utils import QueryTypes
from Common.utils import prefix_dict

class QueryBuilder():
    def __init__(self) -> None:

        self.base_query = ''
        self.prefixes = ''
        self.query_type = ''
        self.distinct = False
        self.vars = ''
        self.query = ''
        self.modifiers = ''
        self.prefix_list = prefix_dict

        self.set_prefixes(['owl','rdfs','rdf'])
        self.set_query(query='')

    def get_query(self) -> str:
        return self.base_query
    
    def set_prefixes(self, prefix: list[str]) -> None:
    
        '''
            Sets prefixes of a query

            ### Parameters
            prefix: list[str] - A list of valid prefix names
        '''
        pref =''

        for var in prefix:
            prefix_uri =  self.prefix_list[var]
            if prefix_uri not in self.prefixes:
                pref += f'PREFIX {var}: {prefix_uri} \n'
        
        self.prefixes += pref
        return self.prefixes  

    def set_modifiers(self, modifiers: dict) -> None:

        '''
            Sets modifiers to the sparql query

            ### Parameters
            modifiers: dict -  A dict of modifiers
        '''
        for key in modifiers:
            self.modifiers += f'{key.upper()} {modifiers[key]} \n'

    def set_query(self, query: str, **kwargs) -> str:
        '''
            Sets the base query for QueryBuilder instance

            ### Required
            query: str -  the query to send to SPARQL endpoint. 

            ### Optional Parameters
            
            query_type:QueryType - The Type of query for the Sparql endpoint, valid values [SELECT,UPDAT,DELETE]
            
            distinct:Bool - A boolean setting the distinct flag for sparql query. Set to False by default.
            
            modifiers:dict - A dict of modifiers, with key as the modifier and value its corrosponding value.
            
            prefixes: list[str] -  A list of prefixes required for sparql query. 
            
            vars: list[str] - A list of variables to return from the query
        '''

        # Set class variables 
        self.query += query

        self.query_type = kwargs.get('query_type', QueryTypes.SELECT).value
        self.distinct = kwargs.get('distinct',False)
        
        self.set_prefixes(kwargs.get('prefixes',[]))
        self.set_modifiers(kwargs.get('modifiers', {}))

        self.vars = ' '. join(kwargs.get('vars',[]))
        

        # Create the base query using the class variables
        self.base_query = f"""{self.prefixes}

        {self.query_type} {'DISTINCT' if self.distinct else ''} {self.vars if self.vars else '*'} WHERE {{
            {self.query if self.query else '{QUERY}'}
        }}
        {self.modifiers}
        """
        return self.base_query