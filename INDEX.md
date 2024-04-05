# OpenSearch Indexing

## Introduction

In OpenSearch, indexing and mapping are fundamental concepts used to organize and structure data. Indexing refers to the process of storing and organizing data in an OpenSearch index, which is similar to a database table. Mapping defines the data types and properties of fields within an index, allowing for efficient searching and retrieval of information.


### dockets index

```
POST dockets/_doc
{
  "agencyId": "IHS", 
  "category": null, 
  "displayProperties": [], 
  "dkAbstract": null, 
  "docketType": "Nonrulemaking", 
  "effectiveDate": null, 
  "field1": null, 
  "field2": null, 
  "generic": null, 
  "keywords": null, 
  "legacyId": null, 
  "modifyDate": "2015-01-10T19:27:21Z", 
  "objectId": "0b000064800f6329", 
  "organization": null, 
  "petitionNbr": null, 
  "program": null, 
  "rin": null, 
  "shortTitle": null, 
  "subType": null, 
  "subType2": null, 
  "title": "Grants and cooperative agreements; availability, etc.: Tribal Self-Governance Program", 
  "id": "IHS-2005-0007", 
  "links": {"self": "https://api.regulations.gov/v4/dockets/IHS-2005-0007"}, 
  "type": "dockets"
}
```

### dockets query

```
GET /dockets/_search
{
  "query": {
    "match": {
      "data.attributes.title": {
        "query": "Tribal Self-governance",
        "fuzziness": "AUTO"
      }
    }
  }
}
```

