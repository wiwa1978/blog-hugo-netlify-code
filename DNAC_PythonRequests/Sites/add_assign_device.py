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
   floor_name = "TESTFLOOR-1"
   
   headers = {
      "Content-Type": "application/json",
      "Accept": "application/json",
      "X-auth-Token": token 
   }  

   # Read in the device configuration to be used in the payload of the REST request
   with open("templates/dummy_device.json", "r") as file:
      payload = json.load(file)

   # Add the device (https://{{dnac}}/dna/intent/api/v1/network-device)
   print("Adding the device")
   device_url = f"{url}/api/v1/network-device"
   response = requests.post(device_url, headers=headers, data=json.dumps(payload), verify=False ).json()
   deviceip = payload["ipAddress"][0]

   # Retrieve the ID of the floor with the provided name
   print("Retrieving the floor ID")
   floor_url = f"/dna/intent/api/v1/site?name=Global/{site_name}/{building_name}/{floor_name}"
   response_floor =  requests.get(url + floor_url, headers=headers, verify=False ).json()
   floor_id = response_floor['response'][0]['id']

   # Call the API to assign the device to the floor with ID floor_id
   print(f"Assign the device to the floor with id {floor_id}")
   site_url = f"{url}/dna/system/api/v1/site/{floor_id}/device" 
   payload = {"device": [{ "ip" : deviceip }]}
   
   response = requests.post(site_url, headers=headers, data=json.dumps(payload), verify=False ).json()
   
   #Check the execution status
   executionStatusUrl = response['executionStatusUrl']

   print("Checking the execution status")
   while True:
      response =  requests.get(url+executionStatusUrl, headers=headers, data=payload, verify=False ).json()
      if response['status'] == "SUCCESS":
         print("Device was successfully assigned")
         break
      else:
         print("Device assignment still in progress")
      time.sleep(1)

if __name__ == "__main__":
   main()
  
