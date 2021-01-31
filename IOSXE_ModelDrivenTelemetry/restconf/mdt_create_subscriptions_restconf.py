import requests
import json

router = {
   'ip': '10.10.20.30',
   'port': '443',
   'username': 'admin',
   'password': 'Cisco123'
}

headers = {
      "Accept" : "application/yang-data+json", 
      "Content-Type" : "application/yang-data+json"
   }

module = "Cisco-IOS-XE-mdt-cfg:mdt-config-data"

url = f"https://{router['ip']}:{router['port']}/restconf/data/{module}"
print(url)

payload = {
    "mdt-config-data": {
        "mdt-subscription": 
            {
                "subscription-id": 100,
                "base": {
                    "stream": "yang-push",
                    "encoding": "encode-kvgpb",
                    "xpath": "/process-cpu-ios-xe-oper:cpu-usage/cpu-utilization/five-seconds",
                    "period": 1000
                },
                "mdt-receivers": {
                    "address": "10.0.19.188",
                    "port": 42518,
                    "protocol": "grpc-tcp"
                }
            }
          }
}

print(payload)

requests.packages.urllib3.disable_warnings()
response = requests.post(url, headers=headers, data=json.dumps(payload), auth=(router['username'], router['password']), verify=False)

print(response)

if (response.status_code == 204):
   print("Successfully updated interface")
else:
   print("Issue with updating interface")
