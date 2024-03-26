"""
This script contains all connections to OpenSearch, including the script to add dockets to 
OpenSearch and the script to query OpenSearch for dockets.
"""

import os
import json
import sys
from dotenv import load_dotenv
import requests

load_dotenv()

username = os.getenv("OPENSEARCH_USERNAME")
password = os.getenv("OPENSEARCH_PASSWORD")

HOST = 'https://search-opensearch334-n6exkzbydhrfh64hs4jw4bo4h4.aos.us-east-1.on.aws'
INDEX = 'dockets'

def get_docket_json(root_folder):
    """ Function to get docket json from data folder."""
    try:
        for root, _, files in os.walk(root_folder):
            if root.split('/')[-1] == 'docket':
                for file in files:
                    if file.endswith('.json'):
                        with open(os.path.join(root, file), encoding='utf-8') as f:
                            docket = json.load(f)
                            add_dockets(docket)
    except FileNotFoundError as e:
        return e
    except json.JSONDecodeError as e:
        return e
    return "Dockets added to OpenSearch."

def get_dockets(search_term):
    """Get dockets from OpenSearch using a search term."""
    url = f"{HOST}/{INDEX}/_search"
    query = {
        "size": 25,
        "query": {
            "match": {
                "data.attributes.title": {
                    "query": search_term,
                    "fuzziness": "AUTO"
                }
            }
        }
    }

    headers = {"Content-Type": "application/json"}

    try:
        r = requests.get(url, auth=(username, password), headers=headers, data=json.dumps(query))
        r.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return

    return r.json()

def add_dockets(docket):
    """Add dockets to OpenSearch."""
    url = f"{HOST}/{INDEX}/_doc"
    headers = {"Content-Type": "application/json"}

    try:
        r = requests.post(url, auth=(username, password), headers=headers, json=docket)
        r.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return

    return r.json()

def main():
    """Directs the script to add to or get dockets from OpenSearch."""
    if len(sys.argv) < 2:
        r = "Usage: python3 opensearch_connection.py [add | get] [search_term]\
              OR python opensearch_connection.py load [data_folder]"
    if sys.argv[1] == "add":
        r = add_dockets(json.loads(sys.argv[2]))
    elif sys.argv[1] == "get":
        r = get_dockets(sys.argv[2])
        print(json.dumps(r, indent=4))
        sys.exit()
    elif sys.argv[1] == "load":
        r = get_docket_json(sys.argv[2])
    else:
        r = "Usage: python3 opensearch_connection.py [add | get] [search_term]\
              OR python opensearch_connection.py load [data_folder]"
    print(r)

if __name__ == "__main__":
    main()
