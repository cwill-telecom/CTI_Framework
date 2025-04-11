"""
Shodan Client: Lookup metadata for a given IP address using the Shodan API
"""

import requests

SHODAN_API_KEY = "your_api_key_here"
BASE_URL = "https://api.shodan.io/shodan/host/"

def lookup_ip(ip):
    url = f"{BASE_URL}{ip}?key={SHODAN_API_KEY}"
    response = requests.get(url)
    return response.json()

if __name__ == "__main__":
    ip = input("Enter IP address to lookup: ")
    result = lookup_ip(ip)
    print(result)
