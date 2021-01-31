import requests
import json
from pprint import pprint


device = {
   'ip': '10.10.20.30',
   'port': '443',
   'username': 'admin',
   'password': 'Cisco123'
}

headers = {
      "Accept" : "application/yang-data+json", 
      "Content-Type" : "application/yang-data+json", 
   }

module = "ietf-interfaces:interfaces"

url = f"https://{device['ip']}:{device['port']}/restconf/data/{module}"
print(url)

requests.packages.urllib3.disable_warnings()
response = requests.get(url, headers=headers, auth=(device['username'], device['password']), verify=False).json()

print(response)
      