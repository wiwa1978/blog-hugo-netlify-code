import requests
from authenticate import get_token
from pprint import pprint


def main():
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

   for device in devices:
      if device['type'] is not None:
         print(f"{device['type']} with serial number {device['serialNumber']}")

if __name__ == "__main__":
   main()