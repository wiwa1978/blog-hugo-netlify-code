import yaml
from pprint import pprint

# Read YAML configuration
yml_file = open("variables.yaml").read()
pprint(yml_file)
yml_dict = yaml.load(yml_file, yaml.SafeLoader)

tenant_name = yml_dict['tenant']
vrf_name = yml_dict['vrf']
bd_name = yml_dict['bridge_domains'][0]['bd']

print("The variables are: ")
print(f"Tenant name {tenant_name}")
print(f"VRF name {vrf_name}")
print(f"BD name {bd_name}")