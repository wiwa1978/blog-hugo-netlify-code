from netmiko import Netmiko

devices = [{
   "device_type": "cisco_xe",
   "ip": "ios-xe-mgmt-latest.cisco.com",
   "username": "developer",
   "password": "C1sco12345",
   "port": "8181",
}]

description = 'Description set with Netmiko'

description_config = [
    "interface GigabitEthernet3",
    f"description {description}",
]

for device in devices:
   net_connect = Netmiko(**device)
   output = net_connect.send_config_set(description_config)
   print(output)
   net_connect.disconnect()
    
    
    