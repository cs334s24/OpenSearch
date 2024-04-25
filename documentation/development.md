## Opensearch Flask Application

Flask App with a front end interface for searching the Mirrulations sample data for dockets by titles. It returns the docket ID, a score, and the docket title.

## Getting Started

Create a .env file in the flask directory with the username and password found in 1Password

```
OPENSEARCH_USERNAME=
OPENSEARCH_PASSWORD=
```

Create a virtual environment

```
python3 -m venv .venv
```

Activate virtual environment

```
source .venv/bin/activate
```

Install requirements

```
pip install -r requirements.txt
```

Launch flask application

```
python3 app.py
```

Acces it via http://localhost:8000

## Running commands manually

`opensearch_connection.py` can be run manually through the terminal as well. 
This will allow you to query, add individual dockets, or load a directory of data.

Follow the steps above through installing the requirements.
To query the data:

```
python3 opensearch_connection.py get <search_term>
```

To add one docket:

```
python3 opensearch_connection.py add <docket_json>
```

To load a directory of data:

```
python3 opensearch_connection.py load <directory>
```

