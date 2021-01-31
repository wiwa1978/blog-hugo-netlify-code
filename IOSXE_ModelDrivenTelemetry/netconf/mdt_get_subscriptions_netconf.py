from ncclient import manager
import xmltodict
import xml.dom.minidom

router = {
   'ip': '10.10.20.30',
   'port': '830',
   'username': 'admin',
   'password': 'Cisco123'
}

netconf_filter = """
    <filter>
       <mdt-config-data xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-mdt-cfg">
         <mdt-subscription>
            <subscription-id></subscription-id>
        </mdt-subscription>
      </mdt-config-data>
    </filter>
"""

m = manager.connect(host=router['ip'], port=router['port'], username=router['username'],
                    password=router['password'], device_params={'name':'iosxe'}, hostkey_verify=False)

running_config = m.get_config('running', netconf_filter)

print(xml.dom.minidom.parseString(str(running_config)).toprettyxml())

m.close_session()

