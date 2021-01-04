import requests
from authenticate import get_token
from pprint import pprint

def main():
   token = get_token()

   dnac = "sandboxdnac2.cisco.com"
   url = f"https://{dnac}/dna/intent/api/v1/"
   family = "Switches and Hubs"

   headers = {
      "Content-Type": "application/json",
      "Accept": "application/json",
      "X-auth-Token": token 
   }

   device_url = url + "network-device?family=" +  family
   response =  requests.get(device_url, headers=headers, verify=False ).json()
   devices = response["response"]

   device_list = []

   for device in devices:
      #print(f"{device['type']} with ID {device['id']}")
      device_list.append(device['id'])
 
   for device_id in device_list:
      print("Investigating device: " + device_id)
      new_interface_url = url + "interface/network-device/" + device_id
      #print(new_interface_url)
      response =  requests.get(new_interface_url, headers=headers, verify=False ).json()
      interfaces = response["response"]
      for interface in interfaces:
         if interface['ipv4Address'] is not None:
            print(f"    {interface['portName']} with IP address {interface['ipv4Address']}")
      


if __name__ == "__main__":
   main()