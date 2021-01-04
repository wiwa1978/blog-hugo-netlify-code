import requests
from authenticate import get_token
from pprint import pprint

def main():
   #dnac = "sandboxdnac2.cisco.com"
   dnac = "10.48.82.183"

   token = get_token(dnac)


   url = f"https://{dnac}/dna/intent/api/v1/site"

   headers = {
      "Content-Type": "application/json",
      "Accept": "application/json",
      "X-auth-Token": token 
   }

   response =  requests.get(url, headers=headers, verify=False ).json()

   sites = response["response"]
   
   sitelist = []
   for site in sites:
      if 'parentId' in site.keys():
         sitelist.append(site['siteNameHierarchy'])
   
   #print(sitelist)

   sitelist.sort()
   for line in sitelist:
      print('   '*line.count('/') + line.split('/')[-1])

if __name__ == "__main__":
   main()