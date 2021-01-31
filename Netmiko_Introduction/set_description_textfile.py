from netmiko import Netmiko
import logging

devices = [{
   "device_type": "cisco_xe",
   "ip": "ios-xe-mgmt-latest.cisco.com",
   "username": "developer",
   "password": "C1sco12345",
   "port": "8181",
}]

logging.basicConfig(filename="test.log", level=logging.DEBUG)
logger = logging.getLogger("netmiko")

for device in devices:
   net_connect = Netmiko(**device)
   output = net_connect.send_config_from_file('changes.txt')
   print(output)
   net_connect.disconnect()
    
    
    