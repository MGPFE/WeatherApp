import requests
import json


def get_weather(CITY):
    API_KEY = "355d0d9b5f1a2e0e585e3f91ae21279e"
    CITY = CITY

    weather = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&units=metric&appid={API_KEY}")
    weather = weather.content.strip()
    weather = weather.decode("utf-8")
    weather = json.loads(weather)

    return weather
