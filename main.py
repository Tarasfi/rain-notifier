import requests
from twilio.rest import Client


OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast?"
api_key = " "#YOURAPI

account_sid = "" #YOURSID
auth_token = "" #YOURTOKEN



weather_params = {
    "lat": "51.9063997", #latitude of city
    "lon": "8.3782078", #longitude of city
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False

for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) <= 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Nimm einen Regenschirm.",
        from_="" #APINUMBER,
        to="" #YOURNUMBER,
    )
    print(message.status)

response.raise_for_status()

