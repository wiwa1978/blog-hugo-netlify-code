import requests
from authenticate import get_token
import json, time
from jinja2 import Environment
from jinja2 import FileSystemLoader

dnac = "10.48.82.183"
token = get_token(dnac)

url = f"https://{dnac}"

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-auth-Token": token 
}

def flowanalysis():
    payload = {
        "sourceIP": "192.168.30.60",
        "destIP": "192.168.13.64",
        "inclusions": [
            "INTERFACE-STATS",
            "DEVICE-STATS",
            "QOS-STATS"
        ],
        "controlPath": False,
        "periodicRefresh": False
    }
      
    flow_url = "/dna/intent/api/v1/flow-analysis"
    print(url + flow_url)
    response_flow =  requests.post(url + flow_url, data=json.dumps(payload), headers=headers, verify=False ).json()
    analysis_url = response_flow['response']['url']
    print(url + analysis_url)
    
    response =  requests.get(url + analysis_url, headers=headers, verify=False ).json()
    print(f"{response['response']['request']['status']}")

if __name__ == "__main__":
   flowanalysis()