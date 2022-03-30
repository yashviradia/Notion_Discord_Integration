import os
import requests
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

INTEGRATION_TOKEN = os.environ.get("INTEGRATION_TOKEN")
DATABASE_ID = os.environ.get("DATABASE_ID")

payload = {
    "page_size": 50,
    "filter": {
      "property": "Fertig",
      "checkbox": {
        "equals": True
      }
    },
}

url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"

headers = {
    "Accept": "application/json",
    "Notion-Version": "2022-02-22",
    "Authorization": f"Bearer {INTEGRATION_TOKEN}",
}

response = requests.request("POST", url, json=payload, headers=headers)


def dictionary_decorder(x):
    return [i for i in x]


title = (response.json()["results"][2]["properties"]["Name"]["title"][0]["plain_text"])
checked = (response.json()["results"][2]["properties"]["Fertig"]["checkbox"])

output_discord = title + "\n" + checked

