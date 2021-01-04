from flask import Flask
from flask import request
import datetime
import requests
import logging
import sys
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

url = "https://api.ciscospark.com/v1/messages"

room_id = "Y2lzY29zcGFyazov*******JjYWMtYTBlMWE3ZTk5OThh"
bearer = "NTgyOThlMmEtOGY*******417f-9974-ad72cae0e10f"

       
@app.route('/', methods = ['GET'])
def index():
    return "<h1>Welcome to this message broker !!</h1>"

@app.route('/message', methods = ['POST'])
def processMessage():
    logging.info('logged in successfully')
    content = request.get_json()
    message = {content['text']}
    print(f"Message: {message}")
 
    sendNotificationToWebexTeams(message, bearer, room_id)
    return "Message sent successfully"

def sendNotificationToWebexTeams(message, bearer, roomId):
   payload = {"roomId": roomId, "text": message}
   headers = {"Authorization": "Bearer %s " % bearer}
   response = requests.post(url, headers=headers, data = payload)
   
if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
