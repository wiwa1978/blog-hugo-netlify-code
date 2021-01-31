import requests
import json
from jinja2 import Environment
from jinja2 import FileSystemLoader
from acicontroller import get_token
from acicontroller import execute_rest_call

JSON_TEMPLATES = Environment(loader=FileSystemLoader('templates'), trim_blocks=True)

def create_bd(tenant_name, vrf_name, bd_name, subnet_ip):
   bd_endpoint = f"api/node/mo/uni/tn-{tenant_name}.json"
   template = JSON_TEMPLATES.get_template("add_bd.j2.json")
   payload = template.render(tenant_name=tenant_name, vrf_name=vrf_name, bd_name=bd_name, subnet_ip=subnet_ip)
   
   response = execute_rest_call(endpoint=bd_endpoint, method="POST", data=payload)
   return response