from ncclient import manager

router = {
   'ip': '10.10.20.30',
   'port': '830',
   'username': 'admin',
   'password': 'Cisco123'
}

netconf_template = open('templates/netconf_mdt_xml.xml').read()
netconf_payload = netconf_template.format(subscription="150", period="5000")

m = manager.connect(host=router['ip'], port=router['port'], username=router['username'],
                    password=router['password'], device_params={'name':'iosxe'}, hostkey_verify=False)

response = m.edit_config(netconf_payload, target="running")
if response.ok:
   print("Subscription added successfully")






