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

module = "ietf-interfaces:interfaces"

url = f"https://{device['ip']}:{device['port']}/restconf/data/{module}"
print(url)

requests.packages.urllib3.disable_warnings()
response = requests.get(url, headers=headers, auth=(device['username'], device['password']), verify=False).json()

interfaces = response['ietf-interfaces:interfaces']['interface']

for interface in interfaces:
   if bool(interface['ietf-ip:ipv4']):
        print(f"{interface['name']} -- {interface['description']} -- {interface['ietf-ip:ipv4']['address'][0]['ip']}")

  
      