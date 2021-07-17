import requests
from datetime import datetime

MY_LAT = 30.152451
MY_LONG = 90.080559


# Simple GET Request
def get_iss_location():
    api_url = "http://api.open-notify.org/iss-now.json"

    response = requests.get(api_url)
    response.raise_for_status()
    data = response.json()

    iss_lat = data["iss_position"]["latitude"]
    iss_lng = data["iss_position"]["longitude"]

    return float(iss_lat), float(iss_lng)


# GET Request with parameters
def get_sunrise():
    api_url = "https://api.sunrise-sunset.org/json"

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get(api_url, params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
    sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

    return int(sunrise), int(sunset)


def is_iss_near_me(iss_lat, iss_lng):
    return (MY_LAT - 5 <= iss_lat <= MY_LAT + 5) and (MY_LONG - 5 <= iss_lng <= MY_LONG + 5)


def is_dark(sunrise, sunset):
    hour = datetime.now().hour
    return sunset <= hour <= sunrise


iss_loc = get_iss_location()
sun_time = get_sunrise()


print("--------------------------------------------")
print("MY LOCATION(LAT, LONG) = ", (MY_LAT, MY_LONG))
print("ISS LOCATION(LAT, LONG) = ", iss_loc)
print("SUNRISE AND SUNSET = ", sun_time)
print("--------------------------------------------")

if is_iss_near_me(*iss_loc) and is_dark(*sun_time):
    print("LOOK UP")
else:
    print("ISS is not above you")
print("--------------------------------------------")
