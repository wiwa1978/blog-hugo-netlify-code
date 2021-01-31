import requests

url = "https://api.ciscospark.com/v1/messages"
room_id = "Y2lzY29zcGFyazovL*******kLWEyZGMtNzQxMDhkMGRiZDU5"
bearer = "Yzg2ZjE4NjAtYWI1MC00NmE*******eb65fdf-9643-417f-9974-ad72cae0e10f"

message =  "### Test message in **markdown**\n\nThis is just to show that markdown is also supported",



payload = {
    "roomId": room_id, 
    "markdown" : message
    }

headers = {
    "Authorization": "Bearer %s " % bearer
    }

response = requests.post(url, headers=headers, data = payload).json()
print(response)
   