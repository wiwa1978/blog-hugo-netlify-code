from ncclient import manager
from pprint import pprint
from jinja2 import Environment
from jinja2 import FileSystemLoader

router = {
   'ip': '10.10.20.30',
   'port': '830',
   'username': 'admin',
   'password': 'Cisco123'
}

my_template = Environment(loader=FileSystemLoader('templates'))

template_vars = {
   "subscription": "200",
   "period": "5000"
}

template = my_template.get_template("netconf_mdt_jinja2.j2")
netconf_payload = template.render(template_vars)

m = manager.connect(host=router['ip'], port=router['port'], username=router['username'],
                    password=router['password'], device_params={'name':'iosxe'}, hostkey_verify=False)

response = m.edit_config(netconf_payload, target="running")

if response.ok:
   print("Subscription added successfully")




