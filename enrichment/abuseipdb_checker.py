"""
AbuseIPDB Checker: Check the reputation of a suspicious IP using AbuseIPDB
"""

import requests

API_KEY = "your_api_key_here"
BASE_URL = "https://api.abuseipdb.com/api/v2/check"

def check_ip(ip):
    headers = {
        "Accept": "application/json",
        "Key": API_KEY
    }
    params = {
        "ipAddress": ip,
        "maxAgeInDays": "90"
    }
    response = requests.get(BASE_URL, headers=headers, params=params)
    return response.json()

if __name__ == "__main__":
    ip = input("Enter IP to check: ")
    result = check_ip(ip)
    print(result)
