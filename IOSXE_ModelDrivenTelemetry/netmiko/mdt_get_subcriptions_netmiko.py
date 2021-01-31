from netmiko import Netmiko

router = {
   'ip': '10.10.20.30',
   'port': '22',
   'username': 'admin',
   'password': 'Cisco123',
   'device_type': 'cisco_xe'
}

net_connect = Netmiko(**router)
output = net_connect.send_command("show telemetry ietf subscription all") 
print(output)
net_connect.disconnect()