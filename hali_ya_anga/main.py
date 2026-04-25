from weather import get_weather , get_forecast
     
def get_emoji(description):
    description = description.lower()

    if "cloud" in description:
        return "☁️"
    if "rain" in description:
        return "🌧️"  
    if "clear" in description:
        return "🌤️"
    if "storm" in description:
        return "⛈️"
    else:
        return "🌡️"

def run():
    print("\n 🌤️DRAFT WEATHER APP🌤️ ")
    print("==========================")

    while True:
        city = input("\nEnter city (or 'q' to quit): ").strip()

        if city.lower() == "q":
            print("Goodbye.")
            break

        if not city:
            print("Please enter a city name.")
            continue

        unit = input("Choose temperature unit - C for Celsius, F for Fahrenheit (default C): ").strip().upper()
        
        if unit == "":
            unit = "C"
        elif unit not in ("C", "F"):
            print("Invalid unit. Please type C or F.")
            continue

        weather = get_weather(city, unit)

        if not weather:
            print("City not found or weather service unavailable.")
            continue
  
        emoji = get_emoji(weather["description"])
        wind_unit = "mph" if unit == "F" else "m/s"
        description = weather["description"].lower()
  
        print(f"\nWeather in {weather['city']}")
        print(f"Temperature: {weather['temperature']} °{unit}")
        print(f"Condition: {weather['description']} {emoji}")
        print(f"Humidity: {weather['humidity']}%")
        print(f"Wind Speed: {weather['wind']} {wind_unit}")

        if unit == "C":
            if weather["temperature"] > 30:
                print("It's hot outside🥵! Stay hydrated.")
            elif weather["temperature"] < 15:
                print("It's freezing! Dress warmly🧥.")
        else:
            if weather["temperature"] > 86:
                print("It's hot outside🥵! Stay hydrated.")
            elif weather["temperature"] < 59:
                print("It's freezing! Dress warmly🧥.")        
        
        if "rain" in description:
            print("☔Don't forget your umbrella!")
        elif "storm" in description:
            print("⚡Better stay indoors for this one😏.")  

        forecast = get_forecast(city , unit)
    
        if forecast:
            print("\n📅 5-Day Forecast:\n")
            
            for item in forecast[:5]:  # Show next 5 forecasts
                emoji = get_emoji(item["desc"])
                print(f"{item['day']:<10}  | 🌡 {item['temp']} °{unit}  | {item['desc']}{emoji}")
        else:
            print("\n📅 Forecast unavailable.")
  
if __name__ == "__main__":
    run()