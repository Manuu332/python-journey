import requests
from config import API_KEY , BASE_URL
from datetime import datetime

weather_cache = {}
forecast_cache = {}

def get_api_unit(unit):
    return "imperial" if unit == "F" else "metric"

def get_weather(city, unit = "C"):
    cache_key = f"{city}_{unit}"
    
    if cache_key in weather_cache:
        return weather_cache[cache_key]
    
    api_unit = get_api_unit(unit)
    url = f"{BASE_URL}/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": api_unit
    }

    try:
        response = requests.get(url , params = params , timeout = 10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error: {e}")
        return None

    data = response.json()

    weather_data = {
        "city": data["name"],
        "temperature": data.get("main", {}).get("temp"),
        "description": data["weather"][0]["description"],
        "humidity": data.get("main", {}).get("humidity"),
        "wind": data.get("wind", {}).get("speed"),
        "icon": data["weather"][0]["icon"],
        "feels_like": data.get("main", {}).get("feels_like"),
    }
    
    weather_cache[cache_key] = weather_data
    
    return weather_data

def get_forecast(city , unit = "C"):
    cache_key = f"{city}_{unit}"

    if cache_key in forecast_cache:
        return forecast_cache[cache_key]
    
    api_unit = get_api_unit(unit)
    url = f"{BASE_URL}/forecast"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": api_unit
    }

    try:
        response = requests.get(url , params = params , timeout = 10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error: {e}")
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
                "icon": item["weather"][0]["icon"],
                })
    
    forecast_cache[cache_key] = forecast_data
    
    return forecast_data[:5]