from flask import Flask,render_template,request
from constants import USER_NAME,PASSWORD
from SPARQLWrapper import SPARQLWrapper, JSON, XML



app = Flask(__name__)

@app.route('/')
# @app.route('/?query_name')
def hello_world():
    var2="mean_age" if request.args.get('query_name', type = str)==None else request.args.get('query_name', type = str)

    print(var2)

    dict_query={"mean_age": r"HasAge Mean (E)", "participants_number": r"HasNumberOfParticipants (E)"}


    sparql = SPARQLWrapper("https://enigma-endpoint.disk.isi.edu/enigma_dev/sparql")

    #To add
    sparql.setCredentials(USER_NAME, PASSWORD)

    sparql.setReturnFormat(JSON)

    new_q=""" PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

    select ?cohortObj ?{} where {{
    ?project ?cohortname ?cohortall .
    ?cohortname rdfs:label "HasCohort (E)" .
    
    ?cohortall ?CohortProj ?cohortProjname .
    ?CohortProj rdfs:label "HasCohortProject (E)" .
    
    ?cohortProjname ?hasParticipants ?{} .
    ?hasParticipants rdfs:label "{}" .
    ?cohortProjname rdfs:label ?cohortObj
    }}

    """.format(var2,var2,dict_query[var2])

    sparql.setQuery(new_q)

    # Convert results to JSON format
    result2 = sparql.query().convert()

    print("Results",result2)


    # For URI, #of participants
    # for hit in result2["results"]["bindings"]:
    #     print(hit["participants"]["datatype"],hit["participants"]["value"])

    # For URI, #of participants
    print("Name: \t\t\t\t\t\t\t\t\t\t\t\t\t\t "+var2)
    for hit in result2["results"]["bindings"]:
        print(hit["cohortObj"]["value"]+" \t\t\t\t\t\t\t "+hit[var2]["value"])

    return result2["results"]["bindings"]



if __name__ == '__main__':
    app.run(debug=True)