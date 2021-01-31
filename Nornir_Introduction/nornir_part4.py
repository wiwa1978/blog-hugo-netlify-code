from nornir import InitNornir
from nornir_scrapli.tasks import (
    get_prompt,
    send_command, send_commands,
    send_configs
)
from nornir_utils.plugins.functions import print_result

nornir = InitNornir('nornir_config.yml')

command_results = nornir.run(task=send_command, command="show ip int brief")
print("Result for DEV01:")
print(command_results["DEV01"].result)

print("Result for DEV02:")
print(command_results["DEV02"].result)

command_results = nornir.run(task=send_commands, commands=["show version", "show ip int brief"])
print("Result for DEV01:")
print(command_results["DEV01"].result)

print("Result for DEV02:")
print(command_results["DEV02"].result)

config_results = nornir.run(
    task=send_configs,
    configs=["interface GigabitEthernet3", "description Configured by Scrapli through Nornir"],
)
print(config_results["DEV01"].result)