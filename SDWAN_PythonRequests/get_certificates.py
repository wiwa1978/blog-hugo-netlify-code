import requests
import json
from authenticate import login
from pprint import pprint

def certificates():
    session = login()

    baseurl = "https://sandboxsdwan.cisco.com:8443"
    #baseurl = "https://10.10.20.90:8443"

    headers = {
        "Accept": "application/json"
    }

    # Get all certificates
    certificate_endpoint = "/dataservice/certificate/vsmart/list"
    url = f"{baseurl}{certificate_endpoint}"
    response_certificate = session.get(url, headers=headers, verify=False).json()
    certificates = response_certificate['data']

    for certificate in certificates:
        print(f"certificate: {certificate['deviceType']} with serial nr {certificate['serialNumber']} expires at {certificate['expirationDate']}  ")

    # Get root certificate
    root_endpoint = "/dataservice/certificate/rootcertificate"
    url = f"{baseurl}{root_endpoint}"
    response_certificate = session.get(url, headers=headers, verify=False).json()
    print(response_certificate['rootcertificate'])
    
if __name__ == "__main__":
   response = certificates()
