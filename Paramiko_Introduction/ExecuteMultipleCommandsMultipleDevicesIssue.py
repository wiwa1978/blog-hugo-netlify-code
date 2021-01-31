import paramiko
from connection import get_connection
import time

devices = {
   'iosxe1': {
      'ip': 'ios-xe-mgmt-latest.cisco.com',
      'username': 'developer',
      'password': 'C1sco12345',
      'port': '8181'
      }
   }

commands = ['show ip interface brief\n', 'show run\n']

for device in devices.keys():
   ssh = get_connection(host=devices[device]['ip'], username=devices[device]['username'], password=devices[device]['password'], port=devices[device]['port'])
   for command in commands:
      stdin, stdout, stderr = ssh.exec_command(command)
      output = stdout.readlines()
      time.sleep(2)
      print(' '.join(map(str, output)))

ssh.close()
