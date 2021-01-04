import requests
import json

def get_token(dnac):  
   url = f"https://{dnac}/dna/system/api/v1/auth/token"

   if dnac=="sandboxdnac2.cisco.com":
      username = "devnetuser"
      password = "---"
   else:
      username = "admin"
      password = "---"

   headers = {
      "Content-Type": "application/json",
   }

   requests.packages.urllib3.disable_warnings()
   response =  requests.post(url, auth=(username, password), verify=False).json()
   #print(response)
   return response["Token"]

if __name__ == "__main__":
   token = get_token()
   #print(token)