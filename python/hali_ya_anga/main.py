from weather import get_weather

def run():
    print("DRAFT WEATHER APP")
    print("-----------------")

    city = input("Enter city: ")

    weather = get_weather(city)

    if not weather:
        print("City not found.")
        return
    
    print(f"\n Weather in {weather['city']}")
    print(f"Temperature:{weather['temperature']}°C")
    print(f"Condition: {weather['description']}")
    print(f"Humidity: {weather['humidity']}%")
    print(f"Wind Speed:{weather['wind']}km/h")

run()          