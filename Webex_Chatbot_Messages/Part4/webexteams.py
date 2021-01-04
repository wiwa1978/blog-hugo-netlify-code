import requests
import json

def send_message(message):
    url = "https://webexteams-messagebot.herokuapp.com/message"

    # to find roomid go to https://developer.webex.com/docs/api/v1/rooms/list-rooms
    room_id = "Y2lzY29zc*******MtYTBlMWE3ZTk5OThh"
    bearer = "NTgyOThlMmEt*******-417f-9974-ad72cae0e10f"

    payload = {
       "roomId": room_id, 
        "text": message
       }

    headers = {
        "Authorization": "Bearer %s " % bearer,
        'Content-Type': 'application/json'
        }

    response = requests.post(url, headers=headers, data =json.dumps(payload))
   
   