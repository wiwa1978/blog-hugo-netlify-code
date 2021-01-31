from napalm import get_network_driver
import json

driver_xr = get_network_driver("iosxr")

device = {
    "device_type": "cisco_xr",
    "ip": "sbx-iosxr-mgmt.cisco.com",
    "username": "admin",
    "password": "C1sco12345",
    "port": "8181",
}

device_xr = driver_xr(hostname=device['ip'], username=device['username'], password=device['password'], optional_args={'port':device['port']})
device_xr.open()
get_method = dir(device_xr)
#print(json.dumps(get_method, sort_keys=True, indent=4))

#get_hostname = device_xr.hostname
#print(f"Hostname is {get_hostname}")

#get_facts = device_xr.get_facts()
#print(json.dumps(get_facts, sort_keys=True, indent=4))

get_interfaces_counters = device_xr.get_interfaces_counters()
print(json.dumps(get_interfaces_counters, sort_keys=True, indent=4))

get_interfaces_ip = device_xr.get_interfaces_ip()
print(json.dumps(get_interfaces_ip, sort_keys=True, indent=4))


