from napalm import get_network_driver
import json

driver_xe = get_network_driver("ios")
driver_xr = get_network_driver("iosxr")

devices = [{
    "device_type": "cisco_xe",
    "ip": "ios-xe-mgmt-latest.cisco.com",
    "username": "developer",
    "password": "C1sco12345",
    "port": "8181",
   },{
    "device_type": "cisco_xr",
    "ip": "sbx-iosxr-mgmt.cisco.com",
    "username": "admin",
    "password": "C1sco12345",
    "port": "8181",
}]

for device in devices:
   if(device['device_type'] == "cisco_xe" ): 
      device_xe = driver_xe(hostname=device['ip'], username=device['username'], password=device['password'], optional_args={'port':device['port']})
      print("Connected to XE")
      print("---------------")
      device_xe.open()
      #print(json.dumps(device_xe.get_interfaces(), sort_keys=True, indent=4))
      for key, value in device_xe.get_interfaces().items() :
         print(key)
      device_xe.close()
   if(device['device_type'] == "cisco_xr" ): 
      device_xr = driver_xr(hostname=device['ip'], username=device['username'], password=device['password'], optional_args={'port':device['port']})
      print("Connected to XR")
      print("---------------")
      device_xr.open()
      for key, value in device_xr.get_interfaces().items() :
         print(key)
      #print(json.dumps(device_xr.get_interfaces(), sort_keys=True, indent=4))
      device_xr.close()
   