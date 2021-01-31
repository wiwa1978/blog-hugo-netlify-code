from netmiko import Netmiko
import logging

logging.basicConfig(filename='test.log', level=logging.DEBUG)
logger = logging.getLogger("netmiko")

cisco_xe = {
    "device_type": "cisco_xe",
    "ip": "ios-xe-mgmt-latest.cisco.com",
    "username": "developer",
    "password": "---",
    "port": "22",
}

net_connect = Netmiko(**cisco_xe)
   
output = net_connect.send_command("show arp")
net_connect.disconnect()
print(output)