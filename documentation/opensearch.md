## **What is Opensearch?**
Opensearch is a tool that allows users to search through the data using unique queries to return more than just a basic term search through Mongo. This is a specifically useful tool for this project as it will allow for you to gain relevancy scores to provide the most relevant information to the user first. With queries, scores will be provided to show which dockets return the most relevant information to the term searched.

## **Our current state**
As it stands as of the end of our Capstone class, we have Opensearch at a point where we have a python program that is interacting with a flask server that allows a user to search a small portion of the sample data and return Dockets matching these parameters with scores from most to least relevant. 

## **How this was achieved**
To get to this point in Opensearch we used the AWS Opensearch instance. We currently have a python program that allows us to ingest large amounts of Dockets into our Opensearch instance. This python program also allows us to search the data set that we have using the built-in Opensearch queries.

## **Roadblocks**
- Needing a larger Opensearch instance to keep up with the large amount of data
- Not having anyone with prior Opensearch knowledge
- Finding a way to implement our current Opensearch code with our API
- Finding a way to search through Documents and Comments, not just Dockets

## What is in our repo
- Flask: Simple flask front end to query the data in a user-friendly way
- .gitignore: Simple gitignore file for files such as a .env
- INDEX.md: Documentation on how the indexes are set up for the data
- README.md: Documentation on how Opensearch works along with some of the queries we found to be helpful for our data 
- development.md: Documentation on how to get the system up and running
- Docker-compose.yml: Simple docker compose file
- Opensearch_connection.py: Our pain python program that allows us to add data to the Opensearch instance as well as query the data 
- Requirements.txt: Simple requirements file

## Helpful links
- [AWS Opensearch documentation](https://docs.aws.amazon.com/opensearch-service/)
- [What is Opensearch](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html)
- [Getting started with Opensearch](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/gsg.html)
