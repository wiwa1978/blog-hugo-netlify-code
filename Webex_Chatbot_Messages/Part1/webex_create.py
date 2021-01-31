import requests

url = "https://api.ciscospark.com/v1/messages"

room_id = "Y2lzY29zcGFyazov*******WEyZGMtNzQxMDhkMGRiZDU5"
bearer = "Yzg2ZjE4NjAtYWI1MC00NmExLW*******-417f-9974-ad72cae0e10f"

message = "This is a test message from the Python application"

payload = {
    "roomId": room_id, 
    "text": message
    }

headers = {
    "Authorization": "Bearer %s " % bearer
    }

response = requests.post(url, headers=headers, data = payload).json()
print(response)
   