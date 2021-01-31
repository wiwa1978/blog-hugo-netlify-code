import paramiko
import time

host = 'ios-xe-mgmt-latest.cisco.com'
username = 'developer'
password = 'C1sco12345'
port = 8181

command = 'show ip interface brief \n'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=host,username=username, password=password, port=port, look_for_keys=False, allow_agent=False)

stdin, stdout, stderr = ssh.exec_command(command)
output = stdout.readlines()
print(' '.join(map(str, output)))
