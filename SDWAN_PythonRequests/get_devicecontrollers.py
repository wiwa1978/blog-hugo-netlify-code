import requests
import json
from authenticate import login

def get_devicecontrollers():
    session = login()

    #baseurl = "https://10.50.221.182:8443"
    baseurl = "https://sandboxsdwan.cisco.com:8443"

    controller_endpoint = "/dataservice/system/device/controllers"
    url = f"{baseurl}{controller_endpoint}"
    print(url)
    response_controller = session.get(url, verify=False)

    devices = response_controller.json()['data']

    for device in devices:
        print(f"Device controller => {device['deviceType']} with IP address {device['deviceIP']}")

if __name__ == "__main__":
   response = get_devicecontrollers()
