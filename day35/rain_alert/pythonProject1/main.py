import os
from twilio.rest import Client

import requests

api_key = "WEATHER API KEY"
#https://api.openweathermap.org/data/2.5/weather?lat=28.704060&lon=77.102493&appid=api_key

url="https://api.openweathermap.org/data/2.5/weather"



auth_token = os.environ.get('AUTH_TOKEN')
account_sid = os.environ.get('OWM_API_KEY')
# OWM_API_KEY=AC4d319531756551c4ddd4f9ce05c75ed8

parameters={
    "lat": 28.704060,
    "lon": 77.102493,
    "appid": api_key,
    "cnt": 4,
}

response= requests.get(url=url, params=parameters)
response.raise_for_status()
data = response.json()
print(data)
weather_data = data["weather"]
print(weather_data)

will_rain = False
for hour_data in weather_data:
    print(hour_data)
    if hour_data["id"] < 700:
        will_rain = True
if True:
    print("Bring an umbrella.")
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Today probably rainy. Don't forget to bring umbrella.",
        from_='+16592167197',
        to='+919458173369'
    )

    print(message.sid)
    print(message.status)
