"""
Pulsedive Feed: Fetch IOCs from the PulseDive platform
"""

import requests

API_KEY = "your_api_key_here"
BASE_URL = "https://api.pulsedive.com/info.php"

def get_indicators(term):
    params = {
        "key": API_KEY,
        "pretty": "1",
        "indicator": term
    }
    response = requests.get(BASE_URL, params=params)
    return response.json()

if __name__ == "__main__":
    indicator = input("Enter IOC (IP/domain/hash) to lookup: ")
    result = get_indicators(indicator)
    print(result)
