from ncclient import manager
from pprint import pprint

router = {
   'host': 'ios-xe-mgmt-latest.cisco.com',
   'port': '10000',
   'username': 'developer',
   'password': 'C1sco12345'
}

netconf_template = open('templates/interface.xml').read()
netconf_payload = netconf_template.format(description="Changing through Netconf")

#print(netconf_payload)

m = manager.connect(host=router['host'], port=router['port'], username=router['username'],
                    password=router['password'], device_params={'name':'iosxe'}, hostkey_verify=False)

response = m.edit_config(netconf_payload, target="running")

print(response)
