import requests
import json
from pprint import pprint


device = {
   "ip": "ios-xe-mgmt-latest.cisco.com",
   "username": "developer",
   "password": "C1sco12345",
   "port": "9443",
}

headers = {
      "Accept" : "application/yang-data+json", 
      "Content-Type" : "application/yang-data+json", 
   }

module = "Cisco-IOS-XE-native:native/interface"

url = f"https://{device['ip']}:{device['port']}/restconf/data/{module}/BDI=60"
print(url)

payload = {
   "Cisco-IOS-XE-native:BDI": 
    {
      "name": "60",
      "description": "Set via RestCONF Python - changed",
    }
 }

requests.packages.urllib3.disable_warnings()
response = requests.put(url, headers=headers, data=json.dumps(payload), auth=(device['username'], device['password']), verify=False)

#print(response)

if (response.status_code == 204):
   print("Successfully updated interface")
else:
   print("Issue with updating interface")


      