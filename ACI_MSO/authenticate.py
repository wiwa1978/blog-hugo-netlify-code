import requests
import json

def get_token():  
   url = f"https://10.48.109.8/api/v1/auth/login"

   payload = {
      "username" : "admin", 
      "password" : "Cisco123456!"
   }

   headers = {
      "Content-Type": "application/json",
   }

   requests.packages.urllib3.disable_warnings()
   response =  requests.post(url, headers=headers, data=json.dumps(payload), verify=False).json()
   return response["token"]

if __name__ == "__main__":
   token = get_token()
