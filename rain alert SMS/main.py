import requests
from twilio.rest import Client

API_KEY = "5113d0f3899a031d33202f0db97f06be"
OWM_endpoint = "https://api.openweathermap.org/data/2.5/weather"
account_sid = "ACf8df2bd539864704fcd245888b3fd5d1"
auth_token = "a39bd4d0e95e1230435f38d15bb02388"

weather_params = {
    # "lat": 28.704060,
    "lat": -33.868820,

    # "lon": 77.102493,
    "lon": 151.209290,

    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_endpoint, params=weather_params)
condition_code = int(response.json()["weather"][0]["id"])

if condition_code < 700:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella☔️",
        from_='+15075744225',
        to='+919818996367'
    )
    print(message.status)

    