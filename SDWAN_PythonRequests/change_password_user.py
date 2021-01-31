import requests
import json
from authenticate import login

def change_password():
    session = login()

    #baseurl = "https://sandboxsdwan.cisco.com:8443"
    baseurl = "https://10.10.20.90:8443"

    payload = {
        "userName": "wim",
        "password": "SuperSecret",
    }

    headers = {
        "Accept": "application/json",
        "Content-Type":  "application/json"
    }

    pwchange_endpoint = "/dataservice/admin/user/password/wim"
    url = f"{baseurl}{pwchange_endpoint}"

    response_pw = session.put(url, headers=headers, data=json.dumps(payload), verify=False)
    print(response_pw.text)
    
if __name__ == "__main__":
   response = change_password()