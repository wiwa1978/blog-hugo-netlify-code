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

module = "ietf-routing:routing/routing-instance=default/routing-protocols/routing-protocol=static,1"

url = f"https://{device['ip']}:{device['port']}/restconf/data/{module}"

requests.packages.urllib3.disable_warnings()
response = requests.get(url, headers=headers, auth=(device['username'], device['password']), verify=False).json()

routes = response['ietf-routing:routing-protocol']['static-routes']

for route in routes['ietf-ipv4-unicast-routing:ipv4']['route']:
    print(f"Route: {route['destination-prefix']} with {route['next-hop']['outgoing-interface']}" )


      