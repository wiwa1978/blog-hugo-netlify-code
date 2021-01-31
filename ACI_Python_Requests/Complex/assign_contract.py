import requests
import json
from jinja2 import Environment
from jinja2 import FileSystemLoader
from acicontroller import get_token
from acicontroller import execute_rest_call

JSON_TEMPLATES = Environment(loader=FileSystemLoader('templates'), trim_blocks=True)

def assign_contract(tenant_name, ap_name, epg_name, contract_name, contract_type):
   assign_contract_endpoint = f"api/node/mo/uni/tn-{tenant_name}/ap-{ap_name}/epg-{epg_name}.json"
   if(contract_type == 'provider'):
      template = JSON_TEMPLATES.get_template("assign_contract_prov.j2.json")
   else:
      template = JSON_TEMPLATES.get_template("assign_contract_cons.j2.json")
   payload = template.render(tenant_name=tenant_name, ap_name=ap_name, epg_name=epg_name, contract_name=contract_name)
   
   response = execute_rest_call(endpoint=assign_contract_endpoint, method="POST", data=payload)
   return response