import tkinter as tk
from weather import get_weather, get_forecast
from PIL import Image , ImageTk
import requests
from io import BytesIO
import geocoder
import threading

SKY_BG = "#171b1d"
CARD_BG = "#ffffff"
TITLE_COLOR = "#133b5c"
TEXT_COLOR = "#244b66"
ACCENT_COLOR = "#0b6e99"
SOFT_COLOR = "#d8ecf5"

recent_cities = []

def threaded_fetch():
    thread = threading .Thread(target = fetch_weather)
    thread.start()

def get_my_city():
    try:
        g = geocoder.ip ('me')
        return g.city if g.city else ""
    except:
        return ""

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

def clear_weather():
    city_entry.delete(0 , tk.END)
    result_label.config(text = "Type city to get started")
    status_label.config(text = "Ready")
    
    my_city = get_my_city()

    if my_city:
        city_entry.insert(0 , my_city)

    city_entry.focus()

def fetch_weather():
    city = city_entry.get().strip()
    unit = unit_var.get()

    if not city:
        result_label.config(text = "❌ Enter city name")
        status_label.config(text = "❌ Waiting for a city name...")
        return

    if city not in recent_cities:
        recent_cities.append(city)
        if len(recent_cities) > 5:
            recent_cities.pop(0)

    status_label.config(text = "⏳ Fetching weather data...")
    search_button.config(state = "disabled")
    root.update_idletasks()

    try:
        weather = get_weather(city , unit)
        
        if not weather:
            result_label.config(text = "❌ City not found or weather service unavailable")
            status_label.config(text = "❌ Error fetching weather data...")
            return

        icon_img = get_icon_image(weather["icon"])
        icon_label.config(image = icon_img)
        icon_label.image = icon_img

        emoji = get_emoji(weather["description"])
        wind_unit = "mph" if unit == "F" else "m/s"

        output = f"📍 {weather['city']}\n"
        output += f"{emoji} {weather['description'].title()}\n"
        output += f"🌡 {weather['temperature']}°{unit}\n"
        output += f"💧 {weather['humidity']}%\n"
        output += f"💨 {weather['wind']} {wind_unit}\n"
        output += f"\n🕒 Recent: \n"
        output += f", ".join(recent_cities)

        forecast = get_forecast(city , unit)

        if forecast:
            output += "\n📅 5-Day Forecast:\n"
            for item in forecast:
                forecast_emoji = get_emoji(item["desc"])
                output += f"{item['day']:<10}: {forecast_emoji} {item['temp']}°{unit}\n\n"
            status_label.config(text ="Weather updated")    
        else:
            output += "\n📅 Forecast unavailable."
            status_label.config(text = "Current weather loaded")        

        result_label.config(text = output)

    finally:
        search_button.config(state = "normal")

def get_icon_image(icon_code):
    url = f"https://openweathermap.org/img/wn/{icon_code}@2x.png"
    response = requests.get(url)
    img_data = response.content
    img = Image.open(BytesIO(img_data))
    return ImageTk.PhotoImage(img)

is_dark = False

def toggle_dark_mode():
    global is_dark
    is_dark = not is_dark

    bg = "#1e1e1e" if is_dark else SKY_BG
    card = "#2b2b2b" if is_dark else CARD_BG
    text = "white" if is_dark else TEXT_COLOR
    
    root.configure(bg = bg)
    app_frame.configure(bg = bg)
    input_card.configure(bg = card)
    result_card.configure(bg = card)

    result_label.configure(bg = card, fg = text)
    status_label.configure(bg = bg, fg = text)
    title_label.configure(bg = bg, fg = text)
    subtitle_label.configure(bg = bg, fg = text)

root = tk.Tk()
root.title("Hali ya Anga 🌞")
root.geometry("430x620")
root.configure(bg = SKY_BG)
root.resizable(False , False)

app_frame = tk.Frame(root , bg = SKY_BG , padx = 20 , pady = 20)
app_frame.pack(fill = "both" , expand = True)

title_label = tk.Label(
    app_frame, 
    text = "Hali ya Anga 🌞" , 
    font = ("Comic Sans" , 22 , "bold"), 
    bg = SKY_BG, 
    fg = TITLE_COLOR,
    )
title_label.pack(anchor = "w")

subtitle_label = tk.Label(
     app_frame, 
     text = "Get current weather and 5-day forecast for any city!",
     font = ("Segoe UI" , 10), 
     bg = SKY_BG, 
     fg = TEXT_COLOR,
    )
subtitle_label.pack(anchor = "w" , pady = (2 , 14))

input_card = tk.Frame(app_frame , bg = CARD_BG , padx = 16 , pady = 16)
input_card.pack(fill = "x")

city_label = tk.Label(
        input_card, 
        text = "City", 
        font = ("Segoe UI" , 10 , "bold"), 
        bg = CARD_BG, 
        fg = TITLE_COLOR,
        )
city_label.pack(anchor = "w")

city_entry = tk.Entry(
        input_card, 
        font = ("Segoe UI" , 12), 
        bd = 0, 
        highlightthickness = 1, 
        highlightbackground = "#9bcde3", 
        highlightcolor = ACCENT_COLOR,
        )
city_entry.pack(fill = "x" , pady = (6 , 12) , ipady = 8)

unit_var = tk.StringVar(value = "C")

unit_frame = tk.Frame(input_card , bg = CARD_BG)
unit_frame.pack(anchor = "w" , pady = (0 , 12))

unit_label = tk.Label(
    unit_frame, 
    text = "Unit", 
    font = ("Segoe UI" , 10 , "bold"), 
    bg = CARD_BG, 
    fg = TITLE_COLOR,
    )
unit_label.pack(side = "left" , padx = (0 , 12))

celsius_button = tk.Radiobutton(
    unit_frame, 
    text = "Celsius", 
    variable = unit_var, 
    value = "C", 
    bg = CARD_BG, 
    fg = TEXT_COLOR, 
    selectcolor = CARD_BG, 
    font = ("Segoe UI" , 10),
    )
celsius_button.pack(side = "left")

fahrenheit_button = tk.Radiobutton(
    unit_frame, 
    text = "Fahrenheit", 
    variable = unit_var, 
    value = "F", 
    bg = CARD_BG, 
    fg = TEXT_COLOR, 
    selectcolor = CARD_BG, 
    font = ("Segoe UI" , 10), 
    )
fahrenheit_button.pack(side = "left" , padx = (10 , 0))

button_frame = tk.Frame(input_card , bg = CARD_BG)
button_frame.pack(fill = "x")

search_button =tk.Button(
    button_frame, 
    text = "Get Weather" , 
    command = threaded_fetch, 
    bg = ACCENT_COLOR, 
    fg = "white", 
    activebackground = "#095675", 
    activeforeground = "white", 
    relief = "flat", 
    font = ("Segoe UI" , 10 , "bold"), 
    padx = 12, 
    pady = 8,
    )
search_button.pack(side = "left")

clear_button = tk.Button(
    button_frame, 
    text = "Clear", 
    command = clear_weather, 
    bg = SOFT_COLOR, 
    fg = TITLE_COLOR, 
    activebackground = "#c5e2ef", 
    relief = "flat", 
    font = ("Segoe UI" , 10), 
    padx = 12, 
    pady = 8, 
    )
clear_button.pack(side = "left" , padx = (10 , 0))

dark_button = tk.Button(
    button_frame, 
    text = "🌚 Dark Mode", 
    command = toggle_dark_mode, 
)
dark_button.pack(side = "right")

status_label = tk.Label(
    app_frame, 
    text = "Ready", 
    font = ("Segoe UI" , 9), 
    bg = SKY_BG,
    fg = TEXT_COLOR, 
    )
status_label.pack(anchor = "w" , pady = (10 , 8))

result_card = tk.Frame(app_frame , bg = CARD_BG , padx = 16 , pady = 16)
result_card.pack(fill = "both" , expand = True)

result_label = tk.Label(
    result_card,  
    text = "Type a city to get started.",  
    justify = "left",  
    anchor = "nw", 
    bg = CARD_BG, 
    fg = TEXT_COLOR, 
    font = ("Segoe UI" , 10), 
    wraplength = 380, 
    )
result_label.pack(fill = "both" , expand = True)

icon_label = tk.Label(result_card , bg = CARD_BG)
icon_label.pack()

root.bind("<Return>" , lambda event : fetch_weather())

my_city = get_my_city()
if my_city:
    city_entry.insert(0 , my_city)
    fetch_weather()

city_entry.focus()

root.mainloop()