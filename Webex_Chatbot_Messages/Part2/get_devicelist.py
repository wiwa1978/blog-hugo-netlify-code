import requests
from authenticate import get_token
from webexteams import send_message
from pprint import pprint


def get_devices():
    dnac = "sandboxdnac2.cisco.com"

    token = get_token(dnac)

    url = f"https://{dnac}/dna/intent/api/v1/network-device"

    headers = {
      "Content-Type": "application/json",
      "Accept": "application/json",
      "X-auth-Token": token 
    }

    response =  requests.get(url, headers=headers, verify=False ).json()
    devices = response["response"]
    #print(devices)

    finaloutput = ""
    for device in devices:
       output = f"hostname: {device['hostname']}, serial: {device['serialNumber']}, platform: {device['serialNumber']}\n"
       finaloutput += output
       #print(output)
    send_message(finaloutput)

if __name__ == "__main__":
   get_devices()