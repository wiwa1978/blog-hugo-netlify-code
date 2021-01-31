import requests
import json
from jinja2 import Environment
from jinja2 import FileSystemLoader
from acicontroller import get_token
from acicontroller import execute_rest_call

JSON_TEMPLATES = Environment(loader=FileSystemLoader('templates'), trim_blocks=True)

def create_filter(tenant_name, filter_name):
   filter_endpoint = f"api/node/mo/uni/tn-{tenant_name}/flt-{filter_name}.json"
   template = JSON_TEMPLATES.get_template("add_filter.j2.json")
   payload = template.render(tenant_name=tenant_name, filter_name=filter_name)
   
   response = execute_rest_call(endpoint=filter_endpoint, method="POST", data=payload)
   return response