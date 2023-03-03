# Query Types Enum
from enum import Enum
class QueryTypes(Enum):
    SELECT = 'SELECT'
    UPDATE = 'UPDATE'
    DELETE = 'DELETE'

prefix_dict = {
  "enigma": "<https://w3id.org/enigma#>",
  "w3id-org": "<https://w3id.org#>",
  "0-1": "<http://xmlns.com/foaf/0.1#>",
  "vaem": "<http://www.linkedmodel.org/schema/vaem#>",
  "owl": "<http://www.w3.org/2002/07/owl#>",
  "rdf": "<http://www.w3.org/1999/02/22-rdf-syntax-ns#>",
  "terms": "<http://purl.org/dc/terms#>",
  "xsd": "<http://www.w3.org/2001/XMLSchema#>",
  "cohort": "<https://w3id.org/enigma/cohort#>",
  "schema-org": "<https://schema.org#>",
  "rdfs": "<http://www.w3.org/2000/01/rdf-schema#>",
  "vann": "<http://purl.org/vocab/vann#>",
  "vcard": "<http://www.w3.org/2006/vcard#>",
  "core": "<http://vivoweb.org/ontology/core#>",
  "foaf": "<http://xmlns.com/foaf#>",
  "bibo": "<http://purl.org/ontology/bibo#>",
  "vann1": "<https://w3id.org/enigmavann:#>",
  "wg": "<https://w3id.org/enigma/wg#>",
  "demographic": "<https://w3id.org/enigma/demographic#>",
  "disorder": "<https://w3id.org/enigma/disorder#>",
  "medication": "<https://w3id.org/enigma/medication#>",
  "psychopathology": "<https://w3id.org/enigma/psychopathology#>",
  "scores": "<https://w3id.org/enigma/scores#>"
}
