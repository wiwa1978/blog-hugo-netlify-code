import paramiko

def get_connection(host, username, password, port):
   ssh = paramiko.SSHClient()
   ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
   ssh.connect(hostname=host,username=username, password=password, port=port, look_for_keys=False, allow_agent=False)
   return ssh