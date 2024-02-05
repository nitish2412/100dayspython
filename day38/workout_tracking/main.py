import requests

APP_ID = "1db787fa"
API_KEY = "76e174af998e292731ee9c2c57bfbc98"
USER_NAME ="nikki007"

api_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
'''
var request = require('request');
var options = {
  'method': 'POST',
  'url': 'https://trackapi.nutritionix.com/v2/natural/exercise',
  'headers': {
    'Content-Type': 'application/json',
    'x-app-id': ,
    'x-app-key':
  },
  body: JSON.stringify({
    "query": "swam for 1 hour"
  })
'''
headers = {
  "x-app-id": APP_ID,
  "x-app-key": API_KEY
}
parameters = {
    "query": "swam for 1 hour"
}

response = requests.post(url=api_endpoint, params=parameters, headers=headers, verify=False)
print(response.text)
