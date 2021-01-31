import requests
import json
from pprint import pprint
from authenticate import login

def get_vedges():
    session = login()

    baseurl = "https://10.50.221.182:8443"

    vedge_endpoint = "/dataservice/system/device/vedges"
    url = f"{baseurl}{vedge_endpoint}"
    
    response_controller = session.get(url, verify=False).json()
    vedges = response_controller['data']

    for vedge in vedges:
        print(f"vEdge device => {vedge['deviceModel']} with serialnumber {vedge['serialNumber']}")

def get_csr1000v():
    session = login()

    baseurl = "https://10.50.221.182:8443"
    controller_endpoint = "/dataservice/system/device/vedges?model=vedge-CSR-1000v"
    url = f"{baseurl}{controller_endpoint}"
    
    response_controller = session.get(url, verify=False).json()
    devices = response_controller['data']

    for device in devices:
        print(f"CSR1000v device => {device['deviceModel']} with serialnumber {device['serialNumber']}")

if __name__ == "__main__":
    print(20 * "--" + "vEdge devices" + 20 * "--" )
    vedges = get_vedges()
    print(20 * "--" + "CSR1000v devices" + 20 * "--" )
    csr1000v = get_csr1000v()
   
   