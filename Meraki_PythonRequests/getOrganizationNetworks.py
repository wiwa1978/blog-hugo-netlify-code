import requests
import json

BASEURL = "https://dashboard.meraki.com/api/v0"

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
     "X-Cisco-Meraki-API-Key": "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
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
        organizations_list.append(organization)

    return organizations_list

def get_organizations_networks(organization_id):
    # Get organization networks
    organization_networks_endpoint = f"/organizations/{organization_id}/networks"
    url = f"{BASEURL}{organization_networks_endpoint}"
    print(url)
    response_organization_network = requests.get(url, headers=headers, verify=False).json()

    organization_networks = response_organization_network
    
    for network in organization_networks:
        print(f"Network ID: {network['id']}")
        print(f"Network Name: {network['name']}")
        print(50* "-")

def get_organizations_inventory(organization_id):
    # Get organization networks
    organization_inventory_endpoint = f"/organizations/{organization_id}/inventory"
    url = f"{BASEURL}{organization_inventory_endpoint}"
    print(url)
    response_organization_inventory = requests.get(url, headers=headers, verify=False).json()

    organization_inventory = response_organization_inventory
    
    for inventory in organization_inventory:
        print(f"Device Serial: {inventory['serial']}")
        print(f"Network Id: {inventory['networkId']}")
        print(50* "-")

def get_organizations_devices(organization_id):
    # Get organization networks
    organization_devices_endpoint = f"/organizations/{organization_id}/devices"
    url = f"{BASEURL}{organization_devices_endpoint}"
    print(url)
    response_organization_devices = requests.get(url, headers=headers, verify=False).json()

    organization_devices = response_organization_devices
    
    for device in organization_devices:
        print(f"Device Model: {device['model']}")
        print(f"Network Id: {device['networkId']}")
        print(50* "-")


if __name__ == "__main__":
    organization_id_list = get_organizations()
    
    for item in organization_id_list:
        print(f"ORGANIZATIONS: {item['name']} with ID {item['id']}")
        #print("ORGANIZATION NETWORKS")
        #get_organizations_networks(item)
        #print("ORGANIZATION INVENTORY")
        #get_organizations_inventory(item)
        #print("ORGANIZATION DEVICES")
        #get_organizations_devices(item)


