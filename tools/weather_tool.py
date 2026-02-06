import os, requests
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    r = requests.get(url).json()
    return {"city": city, "temp": r["main"]["temp"], "description": r["weather"][0]["description"]}
