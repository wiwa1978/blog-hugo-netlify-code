import requests
import json
from authenticate import login
from pprint import pprint

def get_feature_templates():
    session = login()

    # baseurl = "https://10.50.221.182:8443"
    baseurl = "https://sandboxsdwan.cisco.com:8443"

    template_endpoint = "/dataservice/template/feature"
    url = f"{baseurl}{template_endpoint}"
    
    response_template = session.get(url, verify=False).json()
    #pprint(response_template)

    templates = response_template['data']

    feature_templates = []

    for template in templates:
        print(f"Template with id {template['templateId']} (Factory Default: {template['factoryDefault']})")
        print(f"Template with id {template['templateId']} (Template Type:   {template['templateType']})")
        feature_templates.append(
            {
                "templateId": template['templateId'],
                "templateType": template['templateType'],   
            }
        )
        for device in template['deviceType']:
            print(f"    Associated device => {device}")

    return feature_templates

if __name__ == "__main__":
   response = get_feature_templates()
#    print(response)
 