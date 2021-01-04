import requests
from authenticate import get_token
import json, time
from jinja2 import Environment
from jinja2 import FileSystemLoader

dnac = "10.48.82.183"
token = get_token(dnac)

url = f"https://{dnac}"

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-auth-Token": token 
}

def get_assurance_events():
    # Get all assurance events
    events_url = "/dna/intent/api/v1/events?tags=ASSURANCE"
    print(url + events_url)
    response_events =  requests.get(url + events_url, headers=headers, verify=False ).json()
    event_list = []

    for event in response_events:
        event_list.append(event['eventId'])
   
    return event_list

def create_webhook_subscription(eventslist):  
    # Create webhook subscription
    payload = [{
        "name": "webhook_test",
        "subscriptionEndpoints": [
            {
                "subscriptionDetails": {
                    "connectorType": "REST",
                    "name": "webhook.site",
                    "description": "Great for testing",
                    "method": "POST",
                    "url": "https://webhook.site/de8361fc-c77e-437a-989b-9f5c223e6209"
                }
            }
        ],
        "filter": {
            "eventIds": eventslist
        }
    }]

    webhook_url = "/dna/intent/api/v1/event/subscription"
    response_webhook =  requests.post(url + webhook_url, data=json.dumps(payload), headers=headers, verify=False ).json()
    return response_webhook['statusUri']
   
def get_event_status(statusUri): 
    response_event_status =  requests.get(url + statusUri, headers=headers, verify=False ).json()
    print(response_event_status['statusMessage'])


if __name__ == "__main__":
   eventslist = get_assurance_events()
   statusUri = create_webhook_subscription(eventslist)
   get_event_status(statusUri)
