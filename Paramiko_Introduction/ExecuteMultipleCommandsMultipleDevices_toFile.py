import paramiko
import time

commands = ['show version\n', 'show run\n']

max_buffer = 65535
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

def get_connection(host, username, password, port):
   ssh = paramiko.SSHClient()
   ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
   ssh.connect(hostname=host,username=username, password=password, port=port, look_for_keys=False, allow_agent=False)
   return ssh

def clear_buffer(connection):
    if connection.recv_ready():
        return connection.recv(max_buffer)


for device in devices.keys(): 
    outputFileName = device + '_output.txt'
    connection = get_connection(host=devices[device]['ip'], username=devices[device]['username'], password=devices[device]['password'], port=devices[device]['port'])
    new_connection = connection.invoke_shell()
    output = clear_buffer(new_connection)
    time.sleep(2)
    new_connection.send("terminal length 0\n")
    output = clear_buffer(new_connection)

    with open(outputFileName, 'wb') as f:
        for command in commands:
           print(f"Executing command {command}")
           new_connection.send(command)
           time.sleep(2)
           output = new_connection.recv(max_buffer)
           f.write(output)
    
    new_connection.close()