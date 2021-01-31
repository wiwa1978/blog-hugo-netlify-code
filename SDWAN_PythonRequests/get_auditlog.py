import requests
import json
from authenticate import login

def get_auditlog():
    session = login()

    baseurl = "https://sandboxsdwan.cisco.com:8443"
    #baseurl = "https://10.10.20.90:8443"

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    # Get alarm count
    auditlog_endpoint = "/dataservice/auditlog"
    url = f"{baseurl}{auditlog_endpoint}"
    response_auditlog = session.get(url, headers=headers, verify=False).json()

    auditlogs = response_auditlog['data']

    for auditlog in auditlogs:
        print(f"Device: {auditlog['logdeviceid']} -- User: {auditlog['loguser']} --  Message: {auditlog['logmessage']} ")
   


if __name__ == "__main__":
   get_auditlog()
