import requests
from authenticate import get_token
from pprint import pprint


def get_tenants():
   token = get_token()

   base_url = f"https://10.48.109.8/api/v1/"
   tenant_url = "tenants"

   headers = {
      "Content-Type": "application/json",
      "Accept": "application/json",
      "Authorization": f"Bearer {token}"
   }

   overview_sites = {
     "5d84ee4a0e0000bc29476f2a": "netsol-fabric-1", 
     "5e303ef41100007d3d586772": "netsol-fabric-2",
     "5f438740130000b2a2c206c8": "aws-eu",
     "5e53f86d1100009093586773": "bea-arch-fabric3",
     "5e53f8a31100009993586774": "bea-arch-fabric4"
   }

   response =  requests.get(f"{base_url}{tenant_url}", headers=headers, verify=False ).json()
   tenants = response["tenants"]

   for tenant in tenants:
      print(f"Tenant: {tenant['displayName']} -- {tenant['id']}")
      for site in tenant["siteAssociations"]:
         print(f"\t{overview_sites[site['siteId']]}")
           
def get_tenants_for_site(sitename_value):
   token = get_token()

   base_url = f"https://10.48.109.8/api/v1/"
   tenant_url = "tenants"

   headers = {
      "Content-Type": "application/json",
      "Accept": "application/json",
      "Authorization": f"Bearer {token}"
   }

   overview_sites = {
     "5d84ee4a0e0000bc29476f2a": "netsol-fabric-1", 
     "5e303ef41100007d3d586772": "netsol-fabric-2",
     "5f438740130000b2a2c206c8": "aws-eu",
     "5e53f86d1100009093586773": "bea-arch-fabric3",
     "5e53f8a31100009993586774": "bea-arch-fabric4"
   }

   for siteid, sitename in overview_sites.items():
      if sitename == sitename_value:
         my_siteid = siteid
       
        

   response =  requests.get(f"{base_url}{tenant_url}", headers=headers, verify=False ).json()
   tenants = response["tenants"]

   for tenant in tenants:
      #print(f"Tenant: {tenant['displayName']} -- {tenant['id']}")
      
      for site in tenant["siteAssociations"]:
         #print(f"\t{overview_sites[site['siteId']]}")
         
         if (site['siteId'] == my_siteid):
            print(f"Found site {sitename_value} in following tenant(s):")
            print(f"\tTenant: {tenant['displayName']} -- {tenant['id']}")
            break
     
      


if __name__ == "__main__":
   #get_tenants_for_site("aws-eu")
   get_tenants()