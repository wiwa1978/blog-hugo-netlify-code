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
cmds = ['show version', 'show ip int brief']

input = device_xr.cli(cmds)

for i in input.keys():
   input[i] = input[i].split('\n')

print(json.dumps(input, sort_keys=True, indent=4))

device_xr.close()