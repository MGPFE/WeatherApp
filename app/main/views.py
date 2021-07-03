from django.shortcuts import render
from main.api.main import get_weather
from datetime import datetime

# Create your views here.


def index(response):
    time = datetime.now()
    hour = time.strftime("%H")
    hour = int(hour)

    if response.method == "POST":
        ct = response.POST.get("ct")
        weather = get_weather(ct)
        print(weather)
        try:
            weather_dict = {
                "main": weather["weather"][0]["main"],
                "desc": weather["weather"][0]["description"],
                "temp": round(int(weather["main"]["temp"])),
                "icon": weather["weather"][0]["icon"],
                "feels_like": round(int(weather["main"]["feels_like"])),
                "wind": round(float(weather["wind"]["speed"]) * 3.6, 2),
                "wind_deg": weather["wind"]["deg"],
                "country": weather["sys"]["country"],
                "city": weather["name"],
                "city_id": weather["id"],
                "pressure": weather["main"]["pressure"],
                "clouds": weather["clouds"]["all"],
                "code": weather["cod"]
            }
            print(weather_dict["code"])
        except KeyError:
            weather_dict = {
                "city": "Please input a valid city",
            }
        return render(response, "main/page/index.html", {
            "weather": weather_dict,
            "hour": hour
            })

    return render(response, "main/page/index.html", {
        "weather": {"city": "Please enter a city"},
        "hour": hour
        })
