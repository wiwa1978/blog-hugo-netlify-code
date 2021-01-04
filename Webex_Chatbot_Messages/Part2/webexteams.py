import requests
import json

def send_message(message):
    url = "https://api.ciscospark.com/v1/messages"
    #url = "https://webexteams-messagebot.herokuapp.com/message"

    # to find roomid go to https://developer.webex.com/docs/api/v1/rooms/list-rooms
    room_id = "Y2lzY29zcGFy*******BlMWE3ZTk5OThh"
    bearer = "NTgyOThlMmEtOGY5Yy0*******7f-9974-ad72cae0e10f"

    payload = {
       "roomId": room_id, 
        "text": message
       }

    headers = {
        "Authorization": "Bearer %s " % bearer,
        'Content-Type': 'application/json'
        }

    response = requests.post(url, headers=headers, data =json.dumps(payload))
   
   