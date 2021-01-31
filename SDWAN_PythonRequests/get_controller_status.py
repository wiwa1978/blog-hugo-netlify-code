import requests
import json
from authenticate import login
from pprint import pprint

def controller_status():
    session = login()

    baseurl = "https://sandboxsdwan.cisco.com:8443"
    #baseurl = "https://10.10.20.90:8443"

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    # Get certificate summary 
    control_endpoint = "/dataservice/device/control/count"
    url = f"{baseurl}{control_endpoint}"
    response_control = session.get(url, headers=headers, verify=False).json()

    statusList = response_control['data'][0]['statusList']

    for status in statusList:
        print(f"{status['count']} {status['message']}")
        
        if not (status['count']) == 0:
            print("  Checking for more details: ")

            detail_endpoint = status['detailsURL']
            url = f"{baseurl}{detail_endpoint}"
            response_detail = session.get(url, headers=headers, verify=False).json()
            #pprint(response_detail)
            
            details = response_detail['data']
            #pprint(details)
            for detail in details:
                print(f"    {detail['device-model']} device with UUID {detail['uuid']} and IP {detail['system-ip']} ")


if __name__ == "__main__":
   response = controller_status()
