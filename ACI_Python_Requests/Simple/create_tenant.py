import requests
import json
from aci_login import get_token

tenant_name = "Tenant_Python"

def create_tenant():
  
   token = get_token()

   url = "https://10.48.109.10/api/mo/uni.json"
   
   payload = {
      "fvTenant": {
         "attributes": {
            "name": tenant_name
         }
      }
   }

   headers = {
      "Cookie" : f"APIC-Cookie={token}", 
   }

   requests.packages.urllib3.disable_warnings()
   response = requests.post(url,data=json.dumps(payload), headers=headers, verify=False)

   if (response.status_code == 200):
      print("Successfully created tenant")
   else:
      print("Issue with creating tenant")

def get_tenant():
   return tenant_name



if __name__ == "__main__":
   create_tenant()