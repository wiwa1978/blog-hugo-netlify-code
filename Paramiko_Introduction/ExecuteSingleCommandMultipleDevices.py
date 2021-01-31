import paramiko
from connection import get_connection
import time

devices = {
   'iosxe1': {
      'ip': 'ios-xe-mgmt-latest.cisco.com',
      'username': 'developer',
      'password': 'C1sco12345',
      'port': '8181'
      },
   'iosxe2': {
      'ip': 'ios-xe-mgmt-latest.cisco.com',
      'username': 'developer',
      'password': 'C1sco12345',
      'port': '8181'
      }
   }

command = 'show ip interface brief \n'

for device in devices.keys(): 
   print(f"Executing on device: {devices[device]['ip']}\n\n")
   ssh = get_connection(host=devices[device]['ip'], username=devices[device]['username'], password=devices[device]['password'], port=devices[device]['port'])
   stdin, stdout, stderr = ssh.exec_command(command)
   output = stdout.readlines()

   print(' '.join(map(str, output)))


