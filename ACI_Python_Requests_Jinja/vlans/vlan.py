import jinja2

template_vars = {
   "vlan_id": 620, 
   "vlan_name": "vlan-620"
}

vlan_template = """
vlan {{ vlan_id }}
   name {{ vlan_name }}
"""

template = jinja2.Template(vlan_template)
print(template.render(template_vars))