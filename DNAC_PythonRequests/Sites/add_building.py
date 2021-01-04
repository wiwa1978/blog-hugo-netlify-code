import requests
from authenticate import get_token
import time
import json
from jinja2 import Environment
from jinja2 import FileSystemLoader


def main():
   #dnac = "sandboxdnac2.cisco.com"
   dnac = "10.48.82.183"

   token = get_token(dnac)

   url = f"https://{dnac}"

   site_name = "TESTSITE"
   building_name = "TESTBUILDING"
   
   jinja_templates = Environment(loader=FileSystemLoader('templates'), trim_blocks=True)
   template = jinja_templates.get_template("building.j2.json")
   payload = template.render(site_name=site_name, building_name=building_name)

   headers = {
      "Content-Type": "application/json",
      "Accept": "application/json",
      "X-auth-Token": token 
   }  

   site_url = "/dna/intent/api/v1/site"
   response =  requests.post(url + site_url, headers=headers, data=payload, verify=False ).json()

   executionStatusUrl = response['executionStatusUrl']
   
   while True:
      response =  requests.get(url+executionStatusUrl, headers=headers, data=payload, verify=False ).json()
      if response['status'] == "SUCCESS":
         print("Building was successfully added")
         break
      else:
         print("Still in progress")
      time.sleep(1)

if __name__ == "__main__":
   main()