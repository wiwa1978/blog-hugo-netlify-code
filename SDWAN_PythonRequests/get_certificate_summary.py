import requests
import json
from authenticate import login

def certificate_summary():
    session = login()

    baseurl = "https://sandboxsdwan.cisco.com:8443"
    #baseurl = "https://10.10.20.90:8443"

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    # Get certificate summary 
    certificate_endpoint = "/dataservice/certificate/stats/summary"
    url = f"{baseurl}{certificate_endpoint}"
    response_certificate = session.get(url, headers=headers, verify=False).json()

    print(f"Invalid certificates: {response_certificate['data'][0]['invalid']}")
    print(f"Certificates Warnings: {response_certificate['data'][0]['warning']}")

if __name__ == "__main__":
   response = certificate_summary()
