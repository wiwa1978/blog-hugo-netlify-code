import requests
import json

BASEURL = "https://dashboard.meraki.com/api/v0"

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
     "X-Cisco-Meraki-API-Key": "066877fd75bd549c08944b759b4613df7182da22"
}

requests.packages.urllib3.disable_warnings()

def get_organizations():
    # Get organization
    organization_endpoint = "/organizations"
    url = f"{BASEURL}{organization_endpoint}"
    response_organization = requests.get(url, headers=headers, verify=False).json()

    organizations = response_organization

    organizations_list = []

    for organization in organizations:
        organizations_list.append(organization['id'])

    return organizations_list

def get_organizations_networks(organization_id):
    # Get organization networks
    organization_networks_endpoint = f"/organizations/{organization_id}/networks"
    url = f"{BASEURL}{organization_networks_endpoint}"
    response_organization_network = requests.get(url, headers=headers, verify=False).json()

    organization_networks = response_organization_network
    
    networkslist=[]

    for network in organization_networks:
        #print(f"Network ID: {network['id']}")
        #print(f"Network Name: {network['name']}")
        #print(50* "-")
        networkslist.append(network['id'])

    return networkslist
    
def get_cameras(network_id):
      # Get organization networks
    cameras_endpoint = f"/networks/{network_id}/devices"
    url = f"{BASEURL}{cameras_endpoint}"
    response_camera_devices = requests.get(url, headers=headers, verify=False).json()

    camera_devices = response_camera_devices
    
    for camera_device in camera_devices:
        print(len(camera_device))
        if len(camera_device) != 0 or len(camera_device) is None:
            print(f"   Device Model: {camera_device['model']}")
            print(f"   Device Serial: {camera_device['serial']}")
            print(50* "-")
        else:
            print(f"   No Devices")
            print(50* "-")


if __name__ == "__main__":
    organization_id_list = get_organizations()
    for item in organization_id_list:
        print("ORGANIZATION NETWORKS")
        networks = get_organizations_networks(item)
        
        for network in networks:
            print(f"Devices for network {network}")
            print(100* "-")
            get_cameras(network)



