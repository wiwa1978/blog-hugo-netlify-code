import requests
import json
from jinja2 import Environment
from jinja2 import FileSystemLoader
from acicontroller import get_token
from acicontroller import execute_rest_call

JSON_TEMPLATES = Environment(loader=FileSystemLoader('templates'), trim_blocks=True)

def create_tenant(tenant_name):
   tenant_endpoint = "api/mo/uni.json"
   template = JSON_TEMPLATES.get_template("add_tenant.j2.json")
   description = f"Tenant {tenant_name} created with Python Requests"
   payload = template.render(name=tenant_name, description=description)
   
   response = execute_rest_call(endpoint=tenant_endpoint, method="POST", data=payload)
   return response