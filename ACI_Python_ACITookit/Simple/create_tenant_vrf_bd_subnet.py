from acitoolkit.acitoolkit import *
import yaml
from pprint import pprint

url = "https://10.48.109.10/"

user = "admin"
pwd = "C1sco123"

session = Session(url, user, pwd)
session.login()

# Read YAML configuration
yml_file = open("variables.yml").read()
yml_dict = yaml.load(yml_file, yaml.SafeLoader)

tenant_name = yml_dict['tenant']
vrf_name = yml_dict['vrf']
bd_name = yml_dict['bridge_domains'][0]['bd']
bd_subnet = yml_dict['bridge_domains'][0]['gateway'] + "/" + yml_dict['bridge_domains'][0]['mask']
bd_l3out = yml_dict['bridge_domains'][0]['l3_out']

# Create ACI objects
tenant = Tenant(tenant_name)
vrf = Context(vrf_name, tenant)
bd = BridgeDomain(bd_name, tenant)
subnet = Subnet('', bd)
subnet.addr = bd_subnet
bd.add_context(vrf)
l3out = OutsideL3(bd_l3out, tenant)
bd.add_l3out(l3out)
bd.add_subnet(subnet)

response = session.push_to_apic(tenant.get_url(), data=tenant.get_json())

print(response)