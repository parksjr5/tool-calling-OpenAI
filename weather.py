import requests
from creds import credentials

def get_weather(lat=42.7336, long=-84.5539, days=5):
    """
    Collects the weather from the last 5 days using tomorrow.io api
    by using the longitude and latitude of the location.
    
    :param lat: latitude of location
    :type lat: float
    :param long: longitude of location
    :type long: float
    :return output['data']['timelines']: five days of weather at hourly cadence
    :rtype: json
    """
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
    output = response.json()
    for i in range(len(output['data']['timelines'][0]['intervals'])):
        for k,v in output['data']['timelines'][0]['intervals'][i]['values'].items():
            output['data']['timelines'][0]['intervals'][i]['values'][k] = str(v)
    print(f"Lat: {lat}, Long: {long}")
    return output['data']['timelines']