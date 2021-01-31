import requests
from authenticate import get_token
from pprint import pprint


def main():
   dnac = "10.48.82.183"

   token = get_token(dnac)

   site_name = "TESTSITE"
   building_name = "TESTBUILDING"
   floor_name = "TESTFLOOR-2"

   url = f"https://{dnac}"

   headers = {
      "Content-Type": "application/json",
      "Accept": "application/json",
      "X-auth-Token": token 
   }

   site_url = f"{url}/dna/intent/api/v1/site?name=Global/{site_name}"
   print(site_url)
   response =  requests.get(site_url, headers=headers, verify=False ).json()
  
   site_id = response['response'][0]['id']
   membership_url = f"{url}/dna/intent/api/v1/membership/{site_id}"
   print(membership_url)
   response =  requests.get(membership_url, headers=headers, verify=False ).json()
   pprint(response)
    


if __name__ == "__main__":
   main()