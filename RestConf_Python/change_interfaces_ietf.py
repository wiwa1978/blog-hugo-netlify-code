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

url = f"https://{device['ip']}:{device['port']}/restconf/data/{module}/interface=Loopback10000"
print(url)

payload = {
   "interface": [
    {
      "name": "Loopback10000",
      "description": "Adding loopback10000 - changed",
      "type": "iana-if-type:softwareLoopback",
      "enabled": "true",
      "ietf-ip:ipv4": {
        "address": [
          {
            "ip": "192.0.2.60",
            "netmask": "255.255.255.255"
          }
        ]
      }
    }
  ]
 }

#print(type(payload))

requests.packages.urllib3.disable_warnings()
response = requests.put(url, headers=headers, data=json.dumps(payload), auth=(device['username'], device['password']), verify=False)

print(response)

if (response.status_code == 204):
   print("Successfully updated interface")
else:
   print("Issue with updating interface")


      