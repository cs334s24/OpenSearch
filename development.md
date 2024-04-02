## Opensearch Flask Application

Flask App with a front end interface for searching the Mirrulations sample data for dockets by titles. It returns the docket ID, a score, and the docket title.

## Getting Started

Create a .env file in the flask directory with the username and password

In the flask directory create a virtual environment

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

Acces it via localhost 