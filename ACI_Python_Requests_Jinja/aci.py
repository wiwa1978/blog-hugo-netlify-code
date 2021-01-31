import requests
import json
from jinja2 import Environment
from jinja2 import FileSystemLoader

JSON_TEMPLATES = Environment(loader=FileSystemLoader('templates'), trim_blocks=True)
url = "https://10.48.109.10/"

def get_token(username, password):
   partial_url = "api/aaaLogin.json"
   template = JSON_TEMPLATES.get_template("login.j2.json")
   payload = template.render(username=username, password=password)
   new_url=url+partial_url
   requests.packages.urllib3.disable_warnings()
   response = requests.post(new_url, data=payload, verify=False).json()
   token = response['imdata'][0]['aaaLogin']['attributes']['token']
   print(token)
   return token

def create_tenant(tenant_name, token):
   partial_url = "api/mo/uni.json"
   template = JSON_TEMPLATES.get_template("tenant.j2.json")
   payload = template.render(name=tenant_name)

   cookies = {'APIC-Cookie': token }
   new_url=url+partial_url
   response = requests.post(new_url, data=payload, cookies=cookies, verify=False)

   if (response.status_code == 200):
      print("Successfully created tenant")
   else:
      print("Issue with creating tenant")

def main():
   token = get_token("admin", "---")
   create_tenant("Tenant_Python_Jinja2", token)

if __name__ == "__main__":
   main()