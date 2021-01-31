import requests
import json
from authenticate import login
from pprint import pprint

def get_templates():
    session = login()

    # baseurl = "https://10.50.221.182:8443"
    baseurl = "https://sandboxsdwan.cisco.com:8443"
    
    template_endpoint = "/dataservice/template/device"
    url = f"{baseurl}{template_endpoint}"
    
    response_template = session.get(url, verify=False).json()
    #pprint(response_template)

    templates = response_template['data']

    for template in templates:
        print(f"Template => {template['deviceType']} with id {template['templateId']}")

    
if __name__ == "__main__":
   response = get_templates()