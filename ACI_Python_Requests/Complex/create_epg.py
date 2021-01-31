import requests
import json
from jinja2 import Environment
from jinja2 import FileSystemLoader
from acicontroller import get_token
from acicontroller import execute_rest_call

JSON_TEMPLATES = Environment(loader=FileSystemLoader('templates'), trim_blocks=True)

def create_epg(tenant_name, ap_name, epg_name):
   epg_endpoint = f"api/node/mo/uni/tn-{tenant_name}/ap-{ap_name}/epg-{epg_name}.json"
   template = JSON_TEMPLATES.get_template("add_epg.j2.json")
   payload = template.render(tenant_name=tenant_name, ap_name=ap_name, epg_name=epg_name)
   
   response = execute_rest_call(endpoint=epg_endpoint, method="POST", data=payload)
   return response