from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from pprint import pprint

#url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

parameters = {
  'id':'1,2'
}

headers = {
  'Accept': 'application/json',
  'X-CMC_PRO_API_KEY': '***',
}

#headers_pro = {
#  'Accept': 'application/json',
#  'X-CMC_PRO_API_KEY': '***',
#}


session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  response =  response.json()
  #print(response['data'])
  for k,v in response['data'].items():
      print(v['name'])
      print(v['quote']['USD']['price'])

except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)