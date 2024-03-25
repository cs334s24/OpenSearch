import os
from dotenv import load_dotenv
import json
import requests

load_dotenv()

username = os.getenv("OPENSEARCH_USERNAME")
password = os.getenv("OPENSEARCH_PASSWORD")

host = 'https://search-opensearch334-n6exkzbydhrfh64hs4jw4bo4h4.aos.us-east-1.on.aws'
index = 'dockets'
url = f"{host}/{index}/_search"

def main():
    query = {
        "size": 25,
        "query": {
            "match": {
                "title": {
                    "query": "Tribal",
                    "fuzziness": "AUTO"
                }
            }
        }
    }

    headers = {"Content-Type": "application/json"}

    try:
        r = requests.post(url, auth=(username, password), headers=headers, data=json.dumps(query))
        r.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return

    print("Response:")
    print(r.text)

if __name__ == "__main__":
    main()
