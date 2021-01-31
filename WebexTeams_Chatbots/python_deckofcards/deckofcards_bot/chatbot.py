from flask import Flask, request, json
import requests
from messenger import Messenger

app = Flask(__name__)
port = 5005

msg = Messenger()
local_url = 'https://wet-ladybug-77.loca.lt'

@app.route('/', methods=['GET', 'POST'])
def index():

    """Receive a notification from Webex Teams and handle it"""
    if request.method == 'GET':
        return f'Request received on local port {port}'
    elif request.method == 'POST':
        if 'application/json' in request.headers.get('Content-Type'):
            # Notification payload, received from Webex Teams webhook
            data = request.get_json()

         
            # Loop prevention, ignore messages which were posted by bot itself.
            # The bot_id attribute is collected from the Webex Teams API
            # at object instatiation.
            
            if msg.bot_id == data.get('data').get('personId'):
                return 'Message from self ignored'
            else:
                # Print the notification payload, received from the webhook
                print(json.dumps(data,indent=4))

                # Collect the roomId from the notification,
                # so you know where to post the response
                # Set the msg object attribute.
                msg.room_id = data.get('data').get('roomId')

                # Collect the message id from the notification, 
                # so you can fetch the message content
                message_id = data.get('data').get('id')
                print(message_id)

                # Get the contents of the received message. 
                msg.get_message(message_id)

                
                # If message starts with '/server', relay it to the web server.
                # If not, just post a confirmation that a message was received.
                if msg.message_text.startswith('/cards'):
                    # Default action is to list send the 'status' command.
                    #try:
                    #    action = msg.message_text.split()[1]
                    #except IndexError:
                    #    action = 'status'
                    #headers = {'Content-Type': 'application/x-www-form-urlencoded'}
                    #data = f'action={action}'
                    #web_server = 'http://localhost:5005/'
                    #msg.reply = requests.post(web_server, headers=headers, data=data).text
                    reply = requests.get('https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1').json()
                    msg.reply = f'The deck of cards returned the following id: {reply["deck_id"]}'
                    msg.post_message(msg.room_id, msg.reply)
                else:
                    msg.reply = f'Bot received message "{msg.message_text}"'
                    msg.post_message(msg.room_id, msg.reply)

                return data
        else: 
            return ('Wrong data format', 400)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port, debug=False)
