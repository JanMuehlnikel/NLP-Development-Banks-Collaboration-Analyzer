"""
Method to acces IATI Datastore API and store data as json
"""

# Dependencies
import requests
import json

def fetch_data(api_key:str, code:str, abbreviation:str, fl_str:str):
    url = "https://api.iatistandard.org/datastore/activity/select"

    # Access the IATI datastore api
    query = {
        "q": f'reporting_org_ref:("{code}")',
        "start": 0, 
        "rows": 1000,  # max 1000 rows per page
        "fl": fl_str
    }

    # set header with api key from /config/KEYS/IATI_KEY
    # gitignore for KEY; need to create IATI Datastore API Key on your own on IATI web page
    headers = {
        "Ocp-Apim-Subscription-Key": api_key
    }

    try:
        all_docs = []
        page = 0

        max_pages = 1
        max_pages_avl = False
        cur_page = -1

        while True:
            if cur_page < max_pages or max_pages_avl == False:
                cur_page += 1
                response = requests.get(url, params=query, headers=headers)
                
                if response.status_code == 200:
                    data = response.json()
                    docs = data.get("response", {}).get("docs", [])
                    if docs:
                        all_docs.extend(docs)
                        query["start"] += len(docs)
                        page += 1
                    else:
                        break
                else:
                    print("Error:", response.status_code)
                    break
            else:
                break

        with open(f"../../src/responses/response_{abbreviation}.json", mode='w', encoding='utf-8') as file:
            json.dump(all_docs, file, ensure_ascii=False, indent=4)
            
        print(f"⮩ {cur_page} page(s) of data from {abbreviation} stored in src/responses/!")

    except requests.exceptions.RequestException as e:
        print("Error:", e)