from nornir import InitNornir
from nornir_utils.plugins.functions import print_result

nornir = InitNornir('nornir_config.yml')
print(nornir.inventory.hosts)

r1 = nornir.inventory.hosts['DEV01']

print(f"Group: {r1.groups}")
print(f"Hostname: {r1.hostname}")
print(f"Username: {r1.username}")
print(f"Password: {r1.password}")