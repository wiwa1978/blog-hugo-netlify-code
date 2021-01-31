from netmiko import Netmiko

device = {
    "device_type": "cisco_xe",
    "host": "ios-xe-mgmt-latest.cisco.com",
    "username": "developer",
    "password": "C1sco12345",
    "secret": "C1sco12345",
    "port": "8181",
}

net_connect = Netmiko(**device)
print(f"Default prompt: {net_connect.find_prompt()}")

net_connect.send_command_timing("disable")
print(f"Disable command: {net_connect.find_prompt()}")

net_connect.enable()
print(f"Enable command: {net_connect.find_prompt()}")
    