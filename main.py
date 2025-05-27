import requests
from twilio.rest import Client

api = 'Your openweather.com api'
OWM_Endpoint = 'Forecast Api'
account_sid = 'Your account sid from twillio website'
auth_token = 'Your auth token from twillio website'

weather_params = {
    'lat': 53.480709,
    'lon': -2.234380,
    'appid': api,
    'cnt': 4,
}

response = requests.get(OWM_Endpoint, weather_params).json()
id = response['list'][0]['weather'][0]['id']
weather = response['list'][0]['weather'][0]['main']

will_rain = False
for hour_data in response['list']:
    condition = hour_data['weather'][0]['id']
    if int(condition) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(body='It is going to rain today. Remember to bring an umbrella ☔.',
                                     from_='From Number',
                                     to='To Number')
