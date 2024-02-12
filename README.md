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

