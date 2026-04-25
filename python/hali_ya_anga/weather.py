import requests
from config import API_KEY , BASE_URL

def get_weather(city):
    params = {"q": city , "appid" : API_KEY , "units" : "metric"}
    response = requests.get(BASE_URL , params = params)

    if response.status_code != 200:
        return None
    data = response.json()
    weather_data = {"city" : data["name"],
                    "temperature" : data["main"]["temp"],
                    "description" : data["weather"][0]["description"],
                    "humidity": data ["main"]["humidity"],
                    "wind" : data["wind"]["speed"]
                    }
    return weather_data