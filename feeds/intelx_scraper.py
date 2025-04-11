"""
IntelX Scraper: Search historical data for emails, domains, and IPs
"""

import requests

API_KEY = "your_api_key_here"
BASE_URL = "https://2.intelx.io"

def search(term):
    headers = {
        "x-key": API_KEY,
        "Content-Type": "application/json"
    }
    payload = {
        "term": term,
        "maxresults": 10,
        "media": 0
    }
    url = f"{BASE_URL}/api/?rl=search"
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

if __name__ == "__main__":
    term = input("Enter term to search on IntelX: ")
    result = search(term)
    print(result)
