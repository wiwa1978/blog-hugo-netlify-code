import requests
import json
from jinja2 import Environment
from jinja2 import FileSystemLoader
from acicontroller import get_token
from acicontroller import execute_rest_call

JSON_TEMPLATES = Environment(loader=FileSystemLoader('templates'), trim_blocks=True)

def create_contract(tenant_name, contract_name):
   contract_endpoint = f"api/node/mo/uni/tn-{tenant_name}/brc-{contract_name}.json"
   template = JSON_TEMPLATES.get_template("add_contract.j2.json")
   payload = template.render(tenant_name=tenant_name, contract_name=contract_name)
   
   response = execute_rest_call(endpoint=contract_endpoint, method="POST", data=payload)
   return response