import requests
import json
from aci_login import get_token

def get_tenants():
   token = get_token()

   url = "https://10.48.109.10/api/node/class/fvTenant.json"
   
   headers = {
      "Cookie" : f"APIC-Cookie={token}", 
   }

   requests.packages.urllib3.disable_warnings()
   response = requests.get(url, headers=headers, verify=False)

   return response

if __name__ == "__main__":
   response = get_tenants().json()
   tenants = response['imdata']
   
   for tenant in tenants:
      print(f"Tenant name: {tenant['fvTenant']['attributes']['name']}")