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

module = "ietf-interfaces:interfaces/interface=GigabitEthernet3"

url = f"https://{device['ip']}:{device['port']}/restconf/data/{module}"
print(url)

payload = {
  "ietf-interfaces:interface": {
    "name": "GigabitEthernet3",
    "description": "Changed again test 12",
    "type": "iana-if-type:ethernetCsmacd",
    "enabled": "false",
    "ietf-ip:ipv4": {
      "address": [
        {
          "ip": "87.2.3.7",
          "netmask": "255.255.255.0"
        }
      ]
    },
    "ietf-ip:ipv6": {
    }
  }
}

requests.packages.urllib3.disable_warnings()
response = requests.patch(url, headers=headers, data=json.dumps(payload), auth=(device['username'], device['password']), verify=False)

print(response)