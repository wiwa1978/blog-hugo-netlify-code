import requests
import json
from aci_login import get_token

def delete_tenant():
   token = get_token()

   url = "https://10.48.109.10/api/mo/uni.json"
   

   payload = {
      "fvTenant": {
         "attributes": {
            "name": "Tenant_Python",
            "status": "deleted"
         }
      }
   }

   headers = {
      "Cookie" : f"APIC-Cookie={token}", 
   }

   requests.packages.urllib3.disable_warnings()
   response = requests.post(url,data=json.dumps(payload), headers=headers, verify=False)
   
   if (response.status_code == 200):
      print("Successfully deleted tenant")
   else:
      print("Issue with deleting tenant")
   

if __name__ == "__main__":
   delete_tenant()