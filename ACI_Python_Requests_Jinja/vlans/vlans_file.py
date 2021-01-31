from jinja2 import Environment
from jinja2 import FileSystemLoader

my_template = Environment(loader=FileSystemLoader('../templates'))

vlans = {
   "620": "VLAN-620",
   "621": "VLAN-621", 
   "622": "VLAN-622", 
   "623": "VLAN-623",  
}

template = my_template.get_template("vlans.j2")
result = template.render(vlans=vlans)
print(result)

