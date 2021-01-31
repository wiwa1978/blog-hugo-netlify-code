import requests
import json

def login():
    #baseurl = "https://10.50.221.182:8443"
    baseurl = "https://sandboxsdwan.cisco.com:8443"
    authentication_endpoint = "/j_security_check"
    
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
    }

    body = {    
        "j_username": "devnetuser",
        "j_password": "Cisco123!",
    }

    session = requests.session()
    requests.packages.urllib3.disable_warnings()

    url = f"{baseurl}{authentication_endpoint}"
    login_response = session.post(url, data=body, verify=False)

    if b'<html>' in login_response.content:
        print("Login Failed")
        import sys
        sys.exit(0)
    else:
        print("Login succeeded")
        return session
        
