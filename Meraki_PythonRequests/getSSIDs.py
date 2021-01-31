import requests
import json
import sys

BASEURL = "https://dashboard.meraki.com/api/v0"

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
     "X-Cisco-Meraki-API-Key": "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
}

requests.packages.urllib3.disable_warnings()

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

def get_ssids(network_id):
    ssid_endpoint = f"/networks/{network_id}/ssids"
    url = f"{BASEURL}{ssid_endpoint}"
    print(url)
    response_ssids = requests.get(url, headers=headers, verify=False).json()

    return response_ssids


def enable_ssids(ssid_id):
    ssid_enable_endpoint = f"/networks/{network_id}/ssids/{ssid_id}"
    url = f"{BASEURL}{ssid_enable_endpoint}"
    print(url)
    ssid_enable = True

    payload = {
      "enabled": ssid_enable
   }

    response_enable_ssids = requests.put(url, headers=headers, json=payload, verify=False).json()
    print(response_enable_ssids)
    return response_enable_ssids


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f'Usage: python getSSIDs <network_id>')
        sys.exit(1)

    organization_id = sys.argv[1]

    print("ORGANIZATION NETWORKS")
    get_organizations_networks(organization_id)
    
    network_id = input('Provide your network ID: ')
    ssids = get_ssids(network_id)

    for ssid in ssids:
        print(f"{ssid['number']} -- {ssid['name']} -- {ssid['enabled']}")

    ssid_id = input('Provide your SSID ID: ')
    enable_ssids(ssid_id)