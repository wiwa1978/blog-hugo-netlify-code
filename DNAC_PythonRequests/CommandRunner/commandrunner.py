import requests
from authenticate import get_token
from pprint import pprint
import json
import time

dnac = "10.48.82.183"
token = get_token(dnac)
url = f"https://{dnac}/dna/intent"

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
     "X-auth-Token": token 
}

def main():
    family = "Switches and Hubs"

    device_url = url + "/api/v1/network-device?family=" +  family
    response =  requests.get(device_url, headers=headers, verify=False ).json()
    devices = response["response"]

    device_list = []

    # Store all device ids in a list
    for device in devices:
        device_list.append(device['id'])

    # Pass the device list into the payload
    payload = {
        "commands": [
            "show ip interface brief"
        ],
        "deviceUuids": device_list
    }

    # Call the command runner endpoint
    command_url = url + "/api/v1/network-device-poller/cli/read-request"
    response = requests.post(command_url, headers=headers, data=json.dumps(payload), verify=False ).json()

    task_url = response['response']['url']
    task = waitTask(url, task_url )
    fileId = json.loads(task['response']['progress'])

    # Once we have the fileID we can parse the file as such and print the result of our command
    processFile(url, fileId['fileId'])

  
def processFile(url, fileid):
    file_url = url + f"/api/v1/file/{fileid}"
    print(f"FileURL: {file_url}")
    response = requests.get(file_url, headers=headers, verify=False ).json()
    print(response[0]['commandResponses']['SUCCESS']['show ip interface brief'])

def waitTask(url, task_url):
   for i in range(10):
      time.sleep(1)
      response_task =  requests.get(url + task_url, headers=headers, verify=False ).json()
      if response_task['response']['isError']:
         print("Error")
      if "endTime" in response_task['response']:
         return response_task

if __name__ == "__main__":
   main()