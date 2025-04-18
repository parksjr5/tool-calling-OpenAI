import requests
from creds import credentials

def get_weather(lat="42.7336", long="-84.5539"):
    weather_api = credentials['weather_api']

    url = f"https://api.tomorrow.io/v4/weather/realtime?location={lat},{long}&apikey={weather_api}"

    headers = {
        "accept": "application/json"
    }

    response = requests.get(url, headers=headers)
    return response