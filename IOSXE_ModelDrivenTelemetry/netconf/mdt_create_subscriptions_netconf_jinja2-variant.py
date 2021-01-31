from ncclient import manager
from jinja2 import Environment
from jinja2 import FileSystemLoader
from yaml import safe_load

router = {
   'ip': '10.10.20.30',
   'port': '830',
   'username': 'admin',
   'password': 'Cisco123'
}

with open("vars/variables.yml", "r") as handle:
    data = safe_load(handle)

my_template = Environment(loader=FileSystemLoader('templates'))
template = my_template.get_template("netconf_mdt_jinja2-variant.j2.xml")
netconf_payload = template.render(data=data)

m = manager.connect(host=router['ip'], port=router['port'], username=router['username'],
                    password=router['password'], device_params={'name':'iosxe'}, hostkey_verify=False)

response = m.edit_config(netconf_payload, target="running")

if response.ok:
   print("Subscription added successfully")




