import requests
from creds import credentials

def get_weather(lat=42.7336, long=-84.5539, days=5):
    weather_api = credentials['weather_api']

    url = f"https://api.tomorrow.io/v4/timelines?apikey={weather_api}"

    headers = {
        "accept": "application/json",
        "accept-encoding": "deflate, gzip, br",
        "content-type": "application/json"
    }

    data = {
        "location": f"{lat}, {long}",
        "fields": ['temperature', "humidityAvg", "windSpeed", "precipitationProbability"],
        "units": "imperial",
        "timesteps" : ["1h"],
        "startTime" : "now",
        "endTime" : f"nowPlus{days}d"
    }

    response = requests.post(url, headers=headers, json=data)
    print(f"Lat: {lat}, Long: {long}")
    return response