from netmiko import Netmiko

cisco_xr = {
    "device_type": "cisco_xr",
    "ip": "sbx-iosxr-mgmt.cisco.com",
    "username": "admin",
    "password": "C1sco12345",
    "port": "8181",
}

net_connect = Netmiko(**cisco_xr)
   
output = net_connect.send_command("show ip interface brief", use_textfsm=True)
net_connect.disconnect()
print(type(output))

for interface in output:
    print(interface['intf'])

