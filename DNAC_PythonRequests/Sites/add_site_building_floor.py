import requests
from authenticate import get_token
from pprint import pprint
import json
from jinja2 import Environment
from jinja2 import FileSystemLoader


def main():
   #dnac = "sandboxdnac2.cisco.com"
   dnac = "10.48.82.183"

   token = get_token(dnac)

   url = f"https://{dnac}/dna/intent/api/v1/site"

   site_name = "TESTSITE"
   building_name = "TESTBUILDING"
   floor_name = "TESTFLOOR"
   
   jinja_templates = Environment(loader=FileSystemLoader('templates'), trim_blocks=True)
   template = jinja_templates.get_template("site_building_floor.j2.json")
   payload = template.render(site_name=site_name, building_name=building_name, floor_name=floor_name)

   print(payload)

   headers = {
      "Content-Type": "application/json",
      "Accept": "application/json",
      "X-auth-Token": token 
   }  

   response =  requests.post(url, headers=headers, data=payload, verify=False )

   print(response)

if __name__ == "__main__":
   main()