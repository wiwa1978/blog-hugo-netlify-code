from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command, netmiko_send_config
from nornir_utils.plugins.functions import print_result

nornir = InitNornir('nornir_config.yml')

result = nornir.run(netmiko_send_command, command_string="show ip int br")#
print_result(result)

r2 = nornir.filter(name="DEV02")

result = r2.run(netmiko_send_command, command_string="show ip int br")#
print_result(result)

description = 'Description set with Nornir Netmiko'

description_config = [
    "interface GigabitEthernet3",
    f"description {description}",
]
   
result = nornir.run(netmiko_send_config, config_commands=description_config)
print_result(result)