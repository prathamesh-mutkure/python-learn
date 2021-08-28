import requests
import os
from datetime import datetime

# Nutritionix API
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2"
APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")
SHEETY_TOKEN = os.getenv("SHEETY_TOKEN")

headers_nutritionix = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

header_sheety = {
    "Authorization": f"Bearer {SHEETY_TOKEN}",
    "Content-Type": "application/json",
}


def get_natural_exercise(query: str,
                         gender: str = "male",
                         weight_kg: float = 70,
                         height_cm: float = 165,
                         age: int = 18,
                         ):
    api_url = f"{NUTRITIONIX_ENDPOINT}/natural/exercise"

    json_data = {
        "query": query,
        "gender": gender,
        "weight_kg": weight_kg,
        "height_cm": height_cm,
        "age": age,
    }

    response = requests.post(url=api_url, json=json_data, headers=headers_nutritionix)
    response.raise_for_status()

    return response.json()


def add_exercise_row(exercise, date: datetime = datetime.now()) -> requests.Response:

    date_string = date.strftime("%d/%m/%Y")
    time_string = date.strftime("%H:%M:%S")

    json_data = {
        "workout": {
            "date": date_string,
            "time": time_string,
            "exercise": exercise["name"].title(),
            "duration": int(exercise["duration_min"]),
            "calories": int(exercise["nf_calories"]),
        }
    }

    response = requests.post(url=SHEETY_ENDPOINT, json=json_data, headers=header_sheety)
    response.raise_for_status()

    return response


user_query = input("Tell me which exercises you did: ")

exercise_data = get_natural_exercise(query=user_query)
exercises = exercise_data["exercises"]

for exercise_json in exercises:
    google_sheet_response = add_exercise_row(exercise=exercise_json)
    print(google_sheet_response.status_code)
