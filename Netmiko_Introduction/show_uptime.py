from netmiko import Netmiko

devices = [{
    "device_type": "cisco_xr",
    "ip": "sbx-iosxr-mgmt.cisco.com",
    "username": "admin",
    "password": "C1sco12345",
    "port": "8181",
}, {
    "device_type": "cisco_xe",
    "ip": "ios-xe-mgmt-latest.cisco.com",
    "username": "developer",
    "password": "C1sco12345",
    "port": "8181",
}]

for device in devices:
    net_connect = Netmiko(**device)
    output = net_connect.send_command("show version")
    net_connect.disconnect()
    result = output.find('uptime is')
    begin = int(result)
    end = begin + 38
    print(device['ip'] + " => " + output[int(begin):int(end)])
    