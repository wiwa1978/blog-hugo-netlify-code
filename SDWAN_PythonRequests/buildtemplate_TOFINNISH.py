import requests
import json
from authenticate import login
from pprint import pprint
from get_template_feature import get_feature_templates

def build_template():
    session = login()

    baseurl = "https://10.10.20.90:8443"

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    # Get all feature templates
    feature_templates = get_feature_templates()

    payload = {
        "templateName": "Basic_template",
        "templateDescription": "Collection of default templates",
        "deviceType": "vsmart",
        "configType": "template",
        "factoryDefault": False,
        "policyId": "",
        "featureTemplateUidRange": [],
        "generalTemplates": feature_templates
    }

    # 
    template_endpoint = "/dataservice/template/device/feature"
    url = f"{baseurl}{template_endpoint}"
    response_template = session.get(url, headers=headers, data=json.dumps(payload), verify=False).json()

    pprint(response_template)


  
    
if __name__ == "__main__":
   response = build_template()
