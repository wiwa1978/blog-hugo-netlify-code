from nornir import InitNornir
#from nornir_netmiko.tasks import netmiko_send_command, netmiko_send_config
#from nornir_napalm.plugins.tasks import napalm_get, napalm_cli
from nornir_utils.plugins.functions import print_result


nornir = InitNornir('nornir_config.yml')

r1 = nornir.inventory.hosts['DEV01']
print(f"Group: {r1.groups}")
print(f"Hostname: {r1.hostname}")
print(f"Username: {r1.username}")
print(f"Password: {r1.password}")

# result = nr.run(netmiko_send_command, command_string="show ip int br")#
# print_result(result)

#result = nr.run(netmiko_send_command, command_string="show version")#
#print_result(result)

#result = nr.run(napalm_get, getters=['get_interfaces'])
#print_result(result)

#r2 = nr.filter(name="DEV02")

#result = r2.run(netmiko_send_command, command_string="show ip int br")#
#print_result(result)

#result = nr.run(task=napalm_get, getters=["interfaces"])
#print_result(result)

#result = nr.run(napalm_cli, commands=['show version', 'show interface brief'])
#print_result(result)

#result = nr.run(netmiko_send_command, commands=['show version', 'show interface brief'])
#print_result(result)



#description = 'Description set with Nornir'

#description_config = [
#    "interface GigabitEthernet3",
#    f"description {description}",
#]
   
#result = nr.run(netmiko_send_config, config_commands=description_config)
#print_result(result)


