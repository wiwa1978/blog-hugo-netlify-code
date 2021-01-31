from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get, napalm_cli
from nornir_utils.plugins.functions import print_result

nornir = InitNornir('nornir_config.yml')

#result = nornir.run(task=napalm_get, getters=["interfaces"])
#print_result(result)

r2 = nornir.filter(name="DEV02")

result = r2.run(napalm_cli, commands=['show version', 'show ip int brief'])
print_result(result)