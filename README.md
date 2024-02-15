## OpenSearch

This repo is for testing OpenSearch with our sample data

## Links

[Quickstart](https://opensearch.org/docs/latest/quickstart/)
[Mapping](https://opensearch.org/docs/latest/field-types/)
[Dashboards](https://opensearch.org/docs/latest/dashboards/)
[Docker-Compose](https://github.com/opensearch-project/documentation-website/blob/2.11/assets/examples/docker-compose.yml)

## Getting Started

Launch docker-compose file

```
docker-compose up -d
```

Confirm the containers are running

```
docker-compose ps
```

Query the OpenSearch REST API to verify the service is running

```
 curl https://localhost:9200 -ku admin:admin
```

Bring the system down

```
docker-compose down
```

## Possible OpenSearch Methods/Algorithms to Use
**TF-IDF (Term Frequency-Inverse Document Frequency):**
- **Description:** TF-IDF is a statistical measure used to evaluate the importance of a term within a document relative to a collection of documents. It calculates a weight for each term in a document based on how frequently it appears in the document and how rare it is across all documents.
- **How it could be used:** For our project, TF-IDF can be utilized to rank documents based on their relevance to a user's input query. We would compute the TF-IDF score for each term in the query and compare it against the TF-IDF scores of terms in the documents. Documents with higher cumulative TF-IDF scores for the query terms are considered more relevant and are ranked accordingly.
- **Pros:**
    - Provides a straightforward way to prioritize documents based on the importance of query terms within them.
    - Effective for handling large volumes of textual data.
- **Cons:**
    - Lacks some contextual meaning.

**BM25 (Best Matching 25):**
- **Description:** BM25 is a probabilistic information retrieval model that calculates the relevance score of a document to a given query based on the frequency of query terms in the document and the length of the document. It's an improved version of TF-IDF, considering factors like document length normalization.
- **How it could be used:** For our project, BM25 can enhance relevance ranking by providing a more sophisticated scoring mechanism compared to TF-IDF. It accounts for factors such as term frequency saturation and document length normalization, resulting in more accurate ranking of documents based on user input queries.
- **Pros:**
    - Offers improved relevance scoring compared to TF-IDF.
    - Robust to variations in document lengths.
- **Cons:**
    - Like TF-IDF, does not inherently capture semantic relationships between words or documents.

**Vector Space Model (VSM):**
- **Description:** The Vector Space Model represents documents and queries as vectors in a multi-dimensional space, where each dimension corresponds to a term. It measures the similarity between documents and queries using cosine similarity, allowing for the capture of semantic similarities between words and documents.
- **How it could be used:** In our project, VSM can be employed to compute the cosine similarity between the user's input query vector and document vectors. Documents with higher cosine similarity scores are considered more relevant to the query and are ranked accordingly.
- **Pros:**
    - Allows for capturing semantic similarities between words and documents.
    - Is very efficient for large amounts of data.
- **Cons:**
    - Requires careful preprocessing of text data and vector representations.
    - Highest learning curve to fully understand and implement.

