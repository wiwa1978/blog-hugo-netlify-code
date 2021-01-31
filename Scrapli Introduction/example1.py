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
responses = conn.send_commands(["show version", "show ip int brief"])

for response in responses:
   print("RESPONSE")
   print("*" * 100)
   print(response.result)
conn.close()