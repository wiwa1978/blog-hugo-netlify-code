import requests
from authenticate import get_token
import time
import json
from jinja2 import Environment
from jinja2 import FileSystemLoader


def main():
   #dnac = "sandboxdnac2.cisco.com"
   dnac = "10.48.82.183"

   token = get_token(dnac)

   url = f"https://{dnac}"

   site_name = "TESTSITE"
   building_name = "TESTBUILDING"
   floor_name = "TESTFLOOR-2"
   
   headers = {
      "Content-Type": "application/json",
      "Accept": "application/json",
      "X-auth-Token": token 
   }  

   # Read in the device configuration to be used in the payload of the REST request
   with open("templates/dummy_device.json", "r") as file:
      payload = json.load(file)

   # Add the device (https://{{dnac}}/dna/intent/api/v1/network-device)
   device_url = f"{url}/api/v1/network-device"
   response = requests.post(device_url, headers=headers, data=json.dumps(payload), verify=False ).json()
   print(response)

if __name__ == "__main__":
   main()
  
