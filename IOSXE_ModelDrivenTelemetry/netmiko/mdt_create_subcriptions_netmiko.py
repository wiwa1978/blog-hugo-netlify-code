from netmiko import Netmiko
from yaml import safe_load
from jinja2 import Environment, FileSystemLoader

router = {
   'ip': '10.10.20.30',
   'port': '22',
   'username': 'admin',
   'password': 'Cisco123',
   'device_type': 'cisco_xe'
}

with open("vars/variables.yml", "r") as handle:
    data = safe_load(handle)

my_template = Environment(loader=FileSystemLoader('templates'))
template = my_template.get_template("netmiko.j2")
netmiko_payload = template.render(data=data)

net_connect = Netmiko(**router)
output = net_connect.send_config_set(netmiko_payload.split('\n')) 
print(f"Added subscriptions successfully. Here are the commands we used:")
print(output)
net_connect.disconnect()