from netmiko import ConnectHandler

cisco_xr = {
    "device_type": "cisco_xr",
    "ip": "sbx-iosxr-mgmt.cisco.com",
    "username": "admin",
    "password": "C1sco12345",
    "port": "8181",
}

cisco_xe = {
    "device_type": "cisco_xe",
    "ip": "ios-xe-mgmt-latest.cisco.com",
    "username": "developer",
    "password": "C1sco12345",
    "port": "8181",
}

for device in (cisco_xr, cisco_xe):
   net_connect = ConnectHandler(**device)
   
   output = net_connect.send_command("show interface description")
   net_connect.disconnect()
   print("-"*100)
   print(output)
   print("-"*100)