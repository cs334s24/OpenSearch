# OpenSearch Indexing

## Introduction

In OpenSearch, indexing and mapping are fundamental concepts used to organize and structure data. Indexing refers to the process of storing and organizing data in an OpenSearch index, which is similar to a database table. Mapping defines the data types and properties of fields within an index, allowing for efficient searching and retrieval of information.

## OpenSearch Pros

**Scalability**
OpenSearch is meant to scale horizontally which means it is good for handling large amount of data.
It can distribute the workload across multiple nodes which will make for efficent retrieval.

**Flexibal Schema**
OpenSearch allows for dynamic mapping.
Also real-time indexing.
Could be useful as our data is ever growing.

**Nested Documents**
Have the ability to represent relationships between entities in different documents.

## OpenSearch Cons

**Learning Curve** 
Understanding different concepts such as mapping and indexing may take time.

**Resource Intensive**
Can be resource intensive in terms of hardware.
More research needs to be done to understand the scalability of resources
and the overall need for our system.

**Cluster Management**
Managing node addition and and removal may be challenging.
This goes along with the learning curve aspect.

# Example Of A Potential Index

### 1. Index for Agency

```
PUT /agency_index
{
  "mappings": {
    "properties": {
      "docket_id": {"type": "keyword"}
    }
  }
}
```

### 2. Index for Binary Data

```
PUT /binary_docket_index
{
  "mappings": {
    "properties": {
      "docket_id": {"type": "keyword"},
      "comment_attachments": {
        "properties": {
          "comment_id": {"type": "keyword"},
          "counter": {"type": "integer"},
          "extension": {"type": "keyword"}
        }
      },
      "document_attachments": {
        "properties": {
          "document_id": {"type": "keyword"},
          "counter": {"type": "integer"},
          "extension": {"type": "keyword"}
        }
      }
    }
  }
}
```

### 3. Index for Text Data

```
PUT /text_docket_index
{
  "mappings": {
    "properties": {
      "docket_id": {"type": "keyword"},
      "comments": {
        "properties": {
          "comment_id": {"type": "keyword"}
        }
      },
      "comments_extracted_text": {
        "properties": {
          "tool_name": {"type": "keyword"},
          "comment_id": {"type": "keyword"},
          "counter": {"type": "integer"},
          "extracted_text": {"type": "text"}
        }
      },
      "docket": {
        "properties": {
          "docket_id": {"type": "keyword"}
        }
      },
      "documents": {
        "properties": {
          "document_id": {"type": "keyword"}
        }
      },
      "documents_extracted_text": {
        "properties": {
          "tool_name": {"type": "keyword"},
          "document_id": {"type": "keyword"},
          "extracted_text": {"type": "text"}
        }
      }
    }
  }
}
```