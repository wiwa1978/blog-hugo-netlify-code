import requests
import json
from authenticate import login

def get_device_control_connections():
    session = login()

    baseurl = "https://sandboxsdwan.cisco.com:8443"
   #baseurl = "https://10.50.221.182:8443"

    params = {
        "deviceId": "4.4.4.60"
    }
    control_endpoint = "/dataservice/device/control/connections"

    url = f"{baseurl}{control_endpoint}"

    response_controlconn = session.get(url, params = params, verify=False)

    connections = response_controlconn.json()['data']

    for conn in connections:
        print(f"Hostname: {conn['vdevice-host-name']} (type: {conn['peer-type']}) with public IP {conn['public-ip']}")


if __name__ == "__main__":
   response = get_device_control_connections()
