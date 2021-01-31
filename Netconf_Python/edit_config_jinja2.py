from ncclient import manager
from jinja2 import Environment
from jinja2 import FileSystemLoader

router = {
   'host': 'ios-xe-mgmt-latest.cisco.com',
   'port': '10000',
   'username': 'developer',
   'password': 'C1sco12345'
}

my_template = Environment(loader=FileSystemLoader('templates'))

template_vars = {
   "description": "Changed again"
}

template = my_template.get_template("interface.j2.xml")
netconf_payload = template.render(template_vars)

# Alternative: it can also be a little easier.
# description = "Changed description"
# template = my_template.get_template("interface.j2.xml")
# netconf_payload = template.render(description=description)
 
print(netconf_payload)

m = manager.connect(host=router['host'], port=router['port'], username=router['username'],
                    password=router['password'], device_params={'name':'iosxe'}, hostkey_verify=False)

response = m.edit_config(netconf_payload, target="running")

print(response)



