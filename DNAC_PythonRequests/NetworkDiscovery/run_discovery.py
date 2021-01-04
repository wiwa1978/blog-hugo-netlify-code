import requests
from authenticate import get_token
from pprint import pprint
import json, time
from jinja2 import Environment
from jinja2 import FileSystemLoader

dnac = "10.48.82.183"
token = get_token(dnac)
url = f"https://{dnac}"

headers = {
      "Content-Type": "application/json",
      "Accept": "application/json",
      "X-auth-Token": token 
   }

def main():
   cred_url = "/api/v1/global-credential"
   credtype = "CLI"
   
   params = {
      "credentialSubType": {credtype}
   }

   discoveryname = "newDiscovery_v13"

   # Part 1: Get Credentials to run the discovery
   cred_list = []
   response =  requests.get(url + cred_url, params=params, headers=headers, verify=False ).json()
   cred_list.append(response["response"][0]["id"])
   #print(cred_list)

   # Part 2: read in the discovery template
   jinja_templates = Environment(loader=FileSystemLoader('templates'), trim_blocks=True)
   template = jinja_templates.get_template("discovery.j2.json")
   payload = template.render(name=discoveryname)
 
   discovery = json.loads(payload)
      
   # In the JSON body, there should also be a globalCredentialIdList key. This is not in the Jinja template
   discovery["globalCredentialIdList"] = cred_list
 
   # Part 3: Run the discovery
   discover_url = f"https://{dnac}/api/v1/discovery"
   response_discovery =  requests.post(discover_url, data=json.dumps(discovery), headers=headers, verify=False ).json()
   task_url = response_discovery['response']['url']
   #print(f"taskUrl => {task_url}")
   #print(f"taskId => {response_discovery['response']['taskId']}")


   # Part 4: Check the task
   task = waitTask(url, task_url )
   discoverId = task['response']['progress']

   # Part 5: Get Discovery Status
   discover_url = f"https://{dnac}/api/v1/discovery/{discoverId}"

   while True:
      response =  requests.get(discover_url, headers=headers, verify=False ).json()
      
      if response['response']['discoveryCondition'] == "Complete":
         print(f"Discovery with id {discoverId} completed successfully")
         print(f"Discovery found {response['response']['numDevices']} devices") 
   # Part 6: Get Discovered Devices
         devices_url = f"https://{dnac}/api/v1/discovery/{discoverId}/network-device"
         response_devices =  requests.get(devices_url, headers=headers, verify=False ).json()
       
         for device in response_devices['response']:
            print(f"Device name: {device['hostname']} with IP address {device['managementIpAddress']}")

         break
      
   time.sleep(10)
 
def waitTask(url, task_url):
   for i in range(10):
      time.sleep(1)
      response_task =  requests.get(url + task_url, headers=headers, verify=False ).json()
      print(response_task)
      if response_task['response']['isError']:
         print("Error")
      if "endTime" in response_task['response']:
         print(response_task['response']['progress'])
         return response_task

if __name__ == "__main__":
   main()