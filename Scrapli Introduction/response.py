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
response = conn.send_command("show version")
print(response) 
print(response.start_time) 
print(response.elapsed_time) 
print(response.finish_time) 
print(response.channel_input) 
print(response.channel_response) 
print(response.result)
conn.close()