from flask import Flask, request, json
import requests
from messenger import Messenger
from aci import get_token, create_tenant

app = Flask(__name__)
port = 5006

msg = Messenger()
local_url = 'https://quick-walrus-17.loca.lt'
#local_url = 'https://fast-forest-55599.herokuapp.com'

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
                    msg.reply = reply['deck_id']
                    msg.post_message(msg.room_id, msg.reply)
                if msg.message_text.startswith('/aci'):
                    createTenant()
                    msg.reply = f'ACI configured'
                    msg.post_message(msg.room_id, msg.reply)
                else:
                    msg.reply = f'Bot received message "{msg.message_text}"'
                    msg.post_message(msg.room_id, msg.reply)

                return data
        else: 
            return ('Wrong data format', 400)

def createTenant():
    token = get_token("admin", "C1sco123")
    create_tenant("Tenant_Python_Chatbot", token)

if __name__ == '__main__':
    def get_webhook_urls():
        webhook_urls = []
        webhooks_api = f'{msg.base_url}/webhooks'
        webhooks = requests.get(webhooks_api, headers=msg.headers)
        if webhooks.status_code != 200:
            webhooks.raise_for_status()
        else:
            for webhook in webhooks.json()['items']:
                webhook_urls.append(webhook['targetUrl'])
        return webhook_urls
    
    def create_webhook(url):
        webhooks_api = f'{msg.base_url}/webhooks'
        data = {
            "name": "Webhook To Chatbot",
            "resource": "all",
            "event": "all",
            "targetUrl": f"{local_url}"
        }
        webhook = requests.post(webhooks_api, headers=msg.headers, data=json.dumps(data))
        if webhook.status_code != 200:
            webhook.raise_for_status()
        else:
            print(f'Webhook to {local_url} created')
        
    webhook_urls = get_webhook_urls()
    local_urls = []
    local_urls.append(local_url)


    print(webhook_urls)
    print(local_urls)
    
    intersect = list(set(local_urls) & set(webhook_urls))
    if intersect:
        print(f'Registered webhook found already: {intersect[0]}')
    else:
        print(f'Creating webhook:  {local_url}')
        create_webhook(local_url)


    app.run(host="0.0.0.0", port=port, debug=False)
