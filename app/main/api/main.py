import requests
import json


def get_weather(CITY):
    API_KEY = ""
    CITY = CITY

    weather = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&units=metric&appid={API_KEY}")
    weather = weather.content.strip()
    weather = weather.decode("utf-8")
    weather = json.loads(weather)

    return weather
