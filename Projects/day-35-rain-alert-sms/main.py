import requests
import os

MY_LAT = "30"
MY_LONG = "60"
API = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = os.getenv("OWM_API_KEY")


def get_weather_data() -> dict:

    params = {
        "lat": MY_LAT,
        "lon": MY_LONG,
        "appid": API_KEY,
        "exclude": "current,minutely,daily"
    }

    response = requests.get(API, params=params)
    response.raise_for_status()

    return response.json()


def should_get_umbrella(hourly_data_list: list) -> bool:

    for hour_data in hourly_data_list:
        weather = hour_data["weather"][0]

        if weather["id"] < 700:
            return True

    return False


data = get_weather_data()
hourly_data = data["hourly"]

is_weather_bad = should_get_umbrella(hourly_data[:12])

if is_weather_bad:
    print("Carry an Umbrella")
