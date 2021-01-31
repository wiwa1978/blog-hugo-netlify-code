from ncclient import manager
import xmltodict
import xml.dom.minidom

router = {
   'host': 'ios-xe-mgmt-latest.cisco.com',
   'port': '10000',
   'username': 'developer',
   'password': 'C1sco12345'
}

m = manager.connect(host=router['host'], port=router['port'], username=router['username'],
                    password=router['password'], device_params={'name':'iosxe'}, hostkey_verify=False)

netconf_filter = """
<filter>
   <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
      <interface>
         <name>GigabitEthernet3</name>
      </interface>
   </interfaces>
</filter>
"""

running_config = m.get(netconf_filter)
print(xml.dom.minidom.parseString(str(running_config)).toprettyxml())

interfaces = xmltodict.parse(running_config.xml)["rpc-reply"]["data"]
interface = interfaces["interfaces"]["interface"]

print(f'Interface name: { interface["name"]["#text"] }')
print(f'Interface description: { interface["description"] }')
print(f'Interface IP address: {  interface["ipv4"]["address"]["ip"] }')
print(f'Interface IP netmask: {  interface["ipv4"]["address"]["netmask"] }')

