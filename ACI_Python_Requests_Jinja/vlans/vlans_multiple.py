import jinja2

vlans = {
   "620": "VLAN-620",
   "621": "VLAN-621", 
   "622": "VLAN-622", 
   "633": "VLAN-623",  
}

template_vars = {
   "vlans": vlans
}


vlan_template = """
{% for vlan_id, vlan_name in vlans.items() %}
vlan {{ vlan_id }}
   name {{ vlan_name }}
{% endfor %}
"""

template = jinja2.Template(vlan_template)
print(template.render(template_vars))