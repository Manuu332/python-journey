import requests
from config import API_KEY , BASE_URL
from datetime import datetime

def get_weather(city, unit = "C"):
    api_unit = "imperial" if unit == "F" else "metric"
    url = f"{BASE_URL}/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": api_unit
    }

    try:
        response = requests.get(url , params = params , timeout = 10)
        response.raise_for_status()
    except requests.RequestException:
        return None

    data = response.json()

    weather_data = {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"],
        "humidity": data["main"]["humidity"],
        "wind": data["wind"]["speed"],
    }
    return weather_data

def get_forecast(city , unit = "C"):
    api_unit = "imperial" if unit == "F" else "metric"
    url = f"{BASE_URL}/forecast"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": api_unit
    }

    try:
        response = requests.get(url , params = params , timeout = 10)
        response.raise_for_status()
    except requests.RequestException:
        return None
    
    data = response.json()

    forecast_data = []

    for item in data["list"]:
        if "12:00:00" in item["dt_txt"]:
            date_str = item["dt_txt"].split(" ")[0]
            date_obj = datetime.strptime(date_str , "%Y-%m-%d")
            day_name = date_obj.strftime("%A")
            
            forecast_data.append({
                "day": day_name,
                "temp": item["main"]["temp"],
                "desc": item["weather"][0]["description"],
                })
    return forecast_data
