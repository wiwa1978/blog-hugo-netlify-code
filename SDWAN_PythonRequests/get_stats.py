import requests
import json
from authenticate import login

def stats():
    session = login()

    baseurl = "https://sandboxsdwan.cisco.com:8443"
    #baseurl = "https://10.10.20.90:8443"

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    # Get alarm count
    alarms_endpoint = "/dataservice/alarms/count"
    url = f"{baseurl}{alarms_endpoint}"
    response_alarms = session.get(url, headers=headers, verify=False).json()

    print(f"Cleared alarms: {response_alarms['data'][0]['cleared_count']}")
    print(f"Count: {response_alarms['data'][0]['count']}")

if __name__ == "__main__":
   response = stats()
