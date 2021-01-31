from scrapli.driver.core import IOSXEDriver

device = {
    "host": "ios-xe-mgmt-latest.cisco.com",
    "auth_username": "developer",
    "auth_password": "C1sco12345",
    "port": 8181,
    "auth_strict_key": False,
}

conn = IOSXEDriver(**device)
conn.open()
response = conn.send_command("show interface Gi3 description")
print("*"* 100)
print(response.result)

conn.send_configs(["interface GigabitEthernet3", "description Configured by Scrapli"])

response = conn.send_command("show interface Gi3 description")
print("*"* 100)
print(response.result)