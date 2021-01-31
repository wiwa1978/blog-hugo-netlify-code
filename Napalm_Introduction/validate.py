from napalm import get_network_driver
import json
import pprint

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

#pprint.pprint(device_xr.get_facts())
#pprint.pprint(device_xr.get_interfaces())

#pprint.pprint(device_xr.compliance_report("validation.yml"))
response = device_xr.compliance_report("validation.yml")
compliance_status = response['complies']
print(f"Overall compliance status: {compliance_status}")
#print(json.dumps(response, sort_keys=True, indent=4))
#for key, value in response.items():
#   print(key)
#   print(value)

