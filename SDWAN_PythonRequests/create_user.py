import requests
import json
from authenticate import login

def create_user():
    session = login()

    baseurl = "https://10.50.221.182:8443"

    payload = {
        "group": ["netadmin"],
        "description": "User Wim",
        "userName": "wim",
        "password": "Cisco123",
    }

    headers = {
        "Accept": "application/json",
        "Content-Type":  "application/json"
    }

    user_endpoint = "/dataservice/admin/user"
    url = f"{baseurl}{user_endpoint}"
  
    response_user = session.post(url, headers=headers, data=json.dumps(payload), verify=False)
    print(response_user.text)
    
if __name__ == "__main__":
   response = create_user()
